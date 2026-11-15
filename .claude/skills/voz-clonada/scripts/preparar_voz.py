#!/usr/bin/env python3
"""Prepara la grabación de referencia para clonar la voz (XTTS-v2).
Uso: preparar_voz.py GRABACION [GRABACION2 ...] [--out DIR]   (por defecto ~/.local/share/voz-usuario)
Con varias grabaciones se unen (más audio y más variedad de entonación = voz más natural).
- Convierte a WAV mono 22,05 kHz, quita ruido de fondo leve y graves molestos,
  normaliza el volumen y recorta silencios de los extremos.
- Parte el audio en trozos de 8-20 s por las pausas (XTTS promedia varias referencias)."""
import os, re, subprocess, sys

args = sys.argv[1:]
out = os.path.expanduser("~/.local/share/voz-usuario")
if "--out" in args:
    i = args.index("--out"); out = os.path.expanduser(args[i + 1]); del args[i:i + 2]
srcs = args
os.makedirs(out, exist_ok=True)
limpio = os.path.join(out, "referencia.wav")
# silencios: solo los de los extremos (inicio y, con areverse, el final)
recorte = "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.15"
filtro = f"highpass=f=70,afftdn=nf=-30,{recorte},areverse,{recorte},areverse,loudnorm=I=-18:TP=-2:LRA=11"
# cada grabación se limpia por separado (recorte de extremos) y luego se unen
ins = [x for p in srcs for x in ("-i", p)]
fc = ";".join(f"[{i}:a]aformat=sample_rates=22050:channel_layouts=mono,{filtro.rsplit(',loudnorm', 1)[0]}[a{i}]" for i in range(len(srcs)))
fc += ";" + "".join(f"[a{i}]" for i in range(len(srcs))) + f"concat=n={len(srcs)}:v=0:a=1,loudnorm=I=-18:TP=-2:LRA=11[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", fc, "-map", "[o]", "-ac", "1", "-ar", "22050", limpio], check=True)
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", limpio]))
# cortes en los silencios (punto medio de cada pausa)
log = subprocess.run(["ffmpeg", "-hide_banner", "-i", limpio, "-af", "silencedetect=n=-38dB:d=0.35", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
ini = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
fin = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
pausas = [(a + b) / 2 for a, b in zip(ini, fin)]
cortes, a = [], 0.0
for p in pausas + [dur]:
    if p - a >= 8 or (p == dur and p - a >= 3):
        cortes.append((a, p)); a = p
for f in os.listdir(out):
    if f.startswith("ref_") and f.endswith(".wav"):
        os.remove(os.path.join(out, f))
for i, (a, b) in enumerate(cortes):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.2f}", "-to", f"{b:.2f}", "-i", limpio,
                    os.path.join(out, f"ref_{i:02d}.wav")], check=True)
    print(f"ref_{i:02d}.wav  {a:6.2f}-{b:6.2f}  ({b - a:.1f} s)")
print(f"total {dur:.1f} s en {len(cortes)} trozos -> {out}")
