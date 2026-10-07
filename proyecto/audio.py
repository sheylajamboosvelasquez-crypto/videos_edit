#!/usr/bin/env python3
"""Paso 3-4 del skill: genera la voz de cada segmento con edge-tts (Salomé),
mide su duración y escribe salida/trabajo/tiempos.json con los tiempos de cada
segmento y de cada `cue` (para animaciones y cortes de clips)."""
import json, os, subprocess, sys

sys.path.insert(0, os.path.dirname(__file__))
from segmentos import SEGMENTOS

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRAB = os.path.join(RAIZ, "salida", "trabajo")
VOZ = os.path.join(TRAB, "voz")
TTS = os.path.expanduser("~/.claude/skills/lab-fisica-narrado/scripts/tts_edge.py")
PY = os.path.expanduser("~/.venvs/lab-fisica/bin/python")
LEAD, TAIL, FPS = 0.35, 0.55, 30
os.makedirs(VOZ, exist_ok=True)


def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).decode())


def cue_t(say, cue, a_dur):
    i = say.find(cue)
    if i < 0:
        raise SystemExit(f"cue no encontrado: {cue!r}")
    # tiempo ≈ proporcional a los caracteres previos (ritmo de voz casi constante)
    return round(LEAD + a_dur * i / len(say), 3)


out, t0 = [], 0.0
for s in SEGMENTOS:
    wav = os.path.join(VOZ, f"{s['id']}.wav")
    if s.get("silent"):
        a = 0.0
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", str(s["silent"]), wav], check=True)
        total = s["silent"]
    else:
        mp3 = os.path.join(VOZ, f"{s['id']}.mp3")
        if not os.path.exists(mp3):
            subprocess.run([PY, "-I", TTS, s["say"], mp3], check=True)
        a = dur(mp3)
        total = LEAD + a + TAIL
        total = round(round(total * FPS) / FPS, 4)
        # voz con silencio al inicio y al final, exactamente `total` segundos
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp3, "-af", f"adelay={int(LEAD*1000)},apad",
                        "-t", f"{total}", "-ar", "48000", "-ac", "1", wav], check=True)
    cues = {}
    v = s["visual"]
    for key in ("items", "eqs", "facts", "cards", "marks", "clips"):
        for it in v.get(key, []):
            if "cue" in it:
                cues[it["cue"]] = cue_t(s["say"], it["cue"], a)
    for key in ("lead", "note", "eq"):
        if isinstance(v.get(key), dict) and "cue" in v[key]:
            cues[v[key]["cue"]] = cue_t(s["say"], v[key]["cue"], a)
    out.append(dict(id=s["id"], start=round(t0, 4), dur=total, voice=a, cues=cues))
    print(f"{s['id']:5s} voz={a:6.2f}s  segmento={total:6.2f}s  inicio={t0:7.2f}s")
    t0 += total

json.dump(out, open(os.path.join(TRAB, "tiempos.json"), "w"), indent=1, ensure_ascii=False)
print(f"TOTAL {t0:.1f}s = {int(t0//60)}:{t0%60:04.1f}")
