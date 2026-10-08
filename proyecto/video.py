#!/usr/bin/env python3
"""Pasos 5-7 del skill: arma el video final.
1. Tarjetas: render con Remotion (una por segmento).
2. Clips del crudo: estabilizados, fondo desenfocado en verticales, rótulo arriba.
3. Une todo, monta la voz (loudnorm), genera subtítulos y los quema.
Uso: video.py VERSION   (por ejemplo: video.py v1)"""
import json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from segmentos import SEGMENTOS, FONDO, FONDO_FIJO

VER = sys.argv[1] if len(sys.argv) > 1 else "v1"
MODO_FONDO = "fondo" in sys.argv[2:]  # v2: grupo de fondo y tarjetas en recuadro
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRAB = os.path.join(RAIZ, "salida", "trabajo")
SEG = os.path.join(TRAB, "seg")
CRUDO = os.path.join(RAIZ, "crudo lab 4.mp4")
REM = os.path.join(RAIZ, "proyecto", "remotion")
CH = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
FONT = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
LEAD = 0.35
T = {t["id"]: t for t in json.load(open(os.path.join(TRAB, "tiempos.json")))}
os.makedirs(SEG, exist_ok=True)
CMDS = []


def run(cmd, **kw):
    CMDS.append(" ".join(c if re.fullmatch(r"[\w./:=,+-]+", c) else repr(c) for c in cmd))
    subprocess.run(cmd, check=True, **kw)


def esc(s):  # texto para drawtext
    return s.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace("%", "\\%")


def footage(s, t, out):
    clips, dur = s["visual"]["clips"], t["dur"]
    starts = [0.0] + [t["cues"][c["cue"]] - 0.15 for c in clips[1:]]
    ends = starts[1:] + [dur]
    parts, ins = [], []
    for i, (c, a, b) in enumerate(zip(clips, starts, ends)):
        d = round(b - a, 3)
        r0, r1, ori = c["r"]
        L = r1 - r0
        if L >= d:
            ss, speed = r0 + (L - d) / 2, 1.0
        else:
            ss, speed = r0, min(d / L, 1.6)  # cámara lenta suave; si no alcanza, se congela el último cuadro
        ins += ["-ss", f"{ss:.3f}", "-t", f"{min(L, d / speed):.3f}", "-i", CRUDO]
        base = f"[{i}:v]setpts=(PTS-STARTPTS)*{speed:.4f},"
        if ori == "v":
            base += ("crop=604:1080:658:0,deshake=rx=32:ry=32,split[f{i}][g{i}];"
                     f"[g{i}]scale=1920:-2,crop=1920:1080,boxblur=30:3,eq=brightness=-0.18[bg{i}];"
                     f"[f{i}]scale=-2:1080[fg{i}];[bg{i}][fg{i}]overlay=(W-w)/2:0,").replace("{i}", str(i))
        else:
            base += "deshake=rx=32:ry=32,crop=1840:1035,scale=1920:1080,"
        lab = esc(c["label"])
        base += (f"tpad=stop_mode=clone:stop_duration={d:.3f},trim=duration={d:.3f},fps=30,format=yuv420p,"
                 f"drawbox=x=96:y=60:w=10:h=64:color=0xc8102e@1:t=fill:enable='gte(t,0.2)',"
                 f"drawtext=fontfile={FONT}:text='{lab}':x=126:y=72:fontsize=40:fontcolor=white:"
                 f"box=1:boxcolor=0x0d1524@0.72:boxborderw=14:alpha='min(1,max(0,(t-0.2)/0.4))',setsar=1[p{i}]")
        parts.append(base)
    n = len(clips)
    fc = ";".join(parts) + ";" + "".join(f"[p{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0,fade=t=in:st=0:d=0.3,fade=t=out:st={dur - 0.35:.3f}:d=0.35[v]"
    run(["ffmpeg", "-v", "warning", "-y", *ins, "-filter_complex", fc, "-map", "[v]", "-t", f"{dur}",
         "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", "30", "-an", out])


def slide(s, out):
    props = os.path.join(TRAB, "props", f"{s['id']}.json")
    run(["npx", "remotion", "render", "src/index.ts", "Slide", out, f"--props={props}", f"--browser-executable={CH}",
         "--chrome-mode=chrome-for-testing", "--codec=h264", "--crf=18", "--muted", "--log=error"], cwd=REM)


# ---- v2: fondo continuo con el video del grupo ----
LENTO = 1.2  # cámara lenta suave del fondo
SEGF = os.path.join(TRAB, "seg_fondo")
_pos = [0, 0.0]  # índice del rango y avance dentro de él (s de fuente)


def tomar(d):
    """Toma `d` segundos de salida del rollo FONDO (a velocidad 1/LENTO), en orden y dando la vuelta."""
    piezas, falta = [], d / LENTO
    while falta > 0.01:
        a, b, o = FONDO[_pos[0]]
        ini = a + _pos[1]
        resto = b - ini
        if resto < 1.0:
            _pos[0] = (_pos[0] + 1) % len(FONDO); _pos[1] = 0.0
            continue
        n = min(resto, falta)
        if 0 < falta - n < 0.6:  # no dejar un pedacito suelto al final
            n = falta
        n = min(n, resto)
        piezas.append((ini, n, o))
        falta -= n
        _pos[1] += n
    return piezas


def capa_fondo(i, ss, n, o, speed):
    c = f"[{i}:v]setpts=(PTS-STARTPTS)*{speed:.4f},"
    if o == "v":
        c += (f"crop=604:1080:658:0,deshake=rx=32:ry=32,split[f{i}][g{i}];"
              f"[g{i}]scale=1920:-2,crop=1920:1080,boxblur=30:3,eq=brightness=-0.22[bg{i}];"
              f"[f{i}]scale=-2:1080[fg{i}];[bg{i}][fg{i}]overlay=30:0,")
    else:
        c += "deshake=rx=32:ry=32,crop=1840:1035,scale=1920:1080,"
    return c + f"fps=30,format=yuv420p,setsar=1[q{i}]"


def con_fondo(s, t, out):
    dur = t["dur"]
    props = json.load(open(os.path.join(TRAB, "props", f"{s['id']}.json")))
    props["panel"] = True
    pp = os.path.join(SEGF, f"{s['id']}_panel.json")
    json.dump(props, open(pp, "w"), ensure_ascii=False)
    mov = os.path.join(SEGF, f"{s['id']}_panel.mov")
    if not os.path.exists(mov):
        run(["npx", "remotion", "render", "src/index.ts", "Slide", mov, f"--props={pp}", f"--browser-executable={CH}",
             "--chrome-mode=chrome-for-testing", "--codec=prores", "--prores-profile=4444", "--pixel-format=yuva444p10le",
             "--image-format=png", "--muted", "--log=error"], cwd=REM)
    if s["id"] in FONDO_FIJO:
        a, b, o = FONDO_FIJO[s["id"]][0]
        piezas, speed = [(a, b - a, o)], max(1.0, dur / (b - a))
    else:
        piezas, speed = tomar(dur), LENTO
    ins, capas = [], []
    for i, (ss, n, o) in enumerate(piezas):
        ins += ["-ss", f"{ss:.3f}", "-t", f"{n:.3f}", "-i", CRUDO]
        capas.append(capa_fondo(i, ss, n, o, speed))
    k = len(piezas)
    fc = (";".join(capas) + ";" + "".join(f"[q{i}]" for i in range(k)) + f"concat=n={k}:v=1:a=0,"
          f"tpad=stop_mode=clone:stop_duration={dur:.3f},trim=duration={dur:.3f},setpts=PTS-STARTPTS[fondo];"
          f"[{k}:v]scale=1220:686,format=yuva420p,setpts=PTS-STARTPTS[pn];"
          f"[fondo][pn]overlay=664:110:format=auto,format=yuv420p,setsar=1[v]")
    run(["ffmpeg", "-v", "warning", "-y", *ins, "-i", mov, "-filter_complex", fc, "-map", "[v]", "-t", f"{dur}",
         "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", "30", "-an", out])


# ---- 1-2. segmentos de video ----
SOLO = os.environ.get("SOLO")
if SOLO:
    s = next(x for x in SEGMENTOS if x["id"] == SOLO)
    if MODO_FONDO and s["visual"]["kind"] != "footage":
        os.makedirs(SEGF, exist_ok=True)
        for x in SEGMENTOS:  # avanzar el rollo hasta este segmento
            if x["id"] == SOLO:
                break
            if x["visual"]["kind"] != "footage" and x["id"] not in FONDO_FIJO:
                tomar(T[x["id"]]["dur"])
        con_fondo(s, T[SOLO], os.path.join(SEGF, f"{SOLO}.mp4"))
    else:
        out = os.path.join(SEG, f"{SOLO}.mp4")
        footage(s, T[SOLO], out) if s["visual"]["kind"] == "footage" else slide(s, out)
    sys.exit(0)
lista = []
for s in SEGMENTOS:
    out = os.path.join(SEG, f"{s['id']}.mp4")
    if MODO_FONDO and s["visual"]["kind"] != "footage":
        os.makedirs(SEGF, exist_ok=True)
        out = os.path.join(SEGF, f"{s['id']}.mp4")
        if not os.path.exists(out):
            con_fondo(s, T[s["id"]], out)
        else:
            tomar(T[s["id"]]["dur"]) if s["id"] not in FONDO_FIJO else None  # mantener el avance del rollo
    elif not os.path.exists(out):
        (footage(s, T[s["id"]], out) if s["visual"]["kind"] == "footage" else slide(s, out))
    lista.append(out)
    print("listo", s["id"])
open(os.path.join(TRAB, "lista_video.txt"), "w").write("".join(f"file '{p}'\n" for p in lista))
open(os.path.join(TRAB, "lista_voz.txt"), "w").write("".join(f"file '{os.path.join(TRAB, 'voz', s['id'] + '.wav')}'\n" for s in SEGMENTOS))

# ---- 3a. voz completa normalizada ----
voz = os.path.join(TRAB, f"voz_{VER}.wav")
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(TRAB, "lista_voz.txt"),
     "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "48000", "-ac", "1", voz])

# ---- 3b. subtítulos: tiempos del montaje real, repartidos por caracteres ----
def trozos(txt, maxc=42):
    out, cur = [], ""
    for w in txt.split():
        if cur and len(cur) + 1 + len(w) > maxc:
            out.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
        if cur.endswith((".", ";", ":", "?")) and len(cur) > 18:
            out.append(cur); cur = ""
    return out + ([cur] if cur else [])

def ts(x):
    ms = int(round(x * 1000)); return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"

srt, k = [], 1
for s in SEGMENTOS:
    t = T[s["id"]]
    if not s["say"]:
        continue
    lines = trozos(s.get("sub") or s["say"])
    # dos líneas por subtítulo cuando ambas son cortas
    cues, i = [], 0
    while i < len(lines):
        if i + 1 < len(lines) and not lines[i].endswith((".", ":", ";")) and len(lines[i]) + len(lines[i + 1]) <= 80:
            cues.append(lines[i] + "\n" + lines[i + 1]); i += 2
        else:
            cues.append(lines[i]); i += 1
    total = sum(len(c) for c in cues)
    a = t["start"] + LEAD
    for c in cues:
        d = t["voice"] * len(c) / total
        srt.append(f"{k}\n{ts(a)} --> {ts(a + d - 0.04)}\n{c}\n"); k += 1; a += d
srtp = os.path.join(TRAB, f"subs_{VER}.srt")
open(srtp, "w").write("\n".join(srt))

# ---- 3c. unión + subtítulos quemados + audio ----
final = os.path.join(RAIZ, "salida", f"lab4_ley_de_ohm_{VER}.mp4")
style = "FontName=Inter,FontSize=16,PrimaryColour=&H00FFFFFF&,OutlineColour=&H50000000&,BackColour=&H50000000&,BorderStyle=3,Outline=0.8,Shadow=0,Alignment=2,MarginV=22"
# concat por filtro (no demuxer): las tarjetas de Remotion y los clips de ffmpeg tienen
# distinto formato de color y base de tiempo, así que se normalizan antes de unir
ins = [x for p in lista for x in ("-i", p)]
n = len(lista)
norm = ";".join(f"[{i}:v]format=yuv420p,setsar=1,fps=30,settb=1/30,setpts=PTS-STARTPTS[s{i}]" for i in range(n))
fc = norm + ";" + "".join(f"[s{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0,subtitles={srtp}:force_style='{style}'[v]"
run(["ffmpeg", "-v", "error", "-y", *ins, "-i", voz,
     "-filter_complex", fc, "-map", "[v]", "-map", f"{n}:a",
     "-c:v", "libx264", "-crf", "19", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", "30",
     "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-shortest", final])
open(os.path.join(TRAB, f"comandos_{VER}.txt"), "w").write("\n\n".join(CMDS))
print("FINAL", final)
