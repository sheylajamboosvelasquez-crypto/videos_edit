#!/usr/bin/env python3
"""Busca la referencia y los ajustes de Chatterbox que más se parecen a la voz real del usuario.
Mide el parecido con el codificador de voz de Chatterbox (similitud coseno entre huellas de voz).
Uso: buscar_parecido.py [--refs-dir ~/.local/share/voz-usuario] [--n 8]
Deja la mejor referencia en ~/.local/share/voz-usuario/ref_chatter.wav y los ajustes en ajustes_chatter.json."""
import argparse, glob, json, os, shutil, subprocess, time
import numpy as np, torch, torchaudio, librosa

ap = argparse.ArgumentParser()
ap.add_argument("--refs-dir", default="~/.local/share/voz-usuario"); ap.add_argument("--n", type=int, default=8)
a = ap.parse_args()
D = os.path.expanduser(a.refs_dir); T = os.path.join(D, "busqueda"); os.makedirs(T, exist_ok=True)
torch.set_num_threads(os.cpu_count() or 4)
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from chatterbox.models.voice_encoder import VoiceEncoder
m = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
ve = m.ve if hasattr(m, "ve") else VoiceEncoder().eval()

def huella(path):
    w, _ = librosa.load(path, sr=16000)
    e = ve.embeds_from_wavs([w], sample_rate=16000)
    e = np.asarray(e).mean(0); return e / np.linalg.norm(e)

real = huella(os.path.join(D, "referencia.wav"))  # toda la voz del usuario
FRASE = "En esta práctica medimos la corriente y el voltaje en cada resistencia. ¿Y qué encontramos? Que la teoría se cumple."

# candidatos de referencia: ventanas de 10 s de toda la grabación
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(D, "referencia.wav")]))
cands = []
for i, t0 in enumerate(np.linspace(0, dur - 10.5, a.n)):
    p = os.path.join(T, f"cand_{i:02d}.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t0:.2f}", "-t", "10", "-i", os.path.join(D, "referencia.wav"), p], check=True)
    cands.append(p)

def probar(ref, expr, cfg, tag):
    out = os.path.join(T, f"{tag}.wav")
    w = m.generate(FRASE, language_id="es", audio_prompt_path=ref, exaggeration=expr, cfg_weight=cfg)
    torchaudio.save(out, w, m.sr)
    s = float(huella(out) @ real)
    print(f"{tag:22s} parecido={s:.3f}", flush=True); return s, out

# 1) mejor referencia con ajustes neutros
res = [(probar(c, 0.5, 0.5, f"ref{i:02d}")[0], c) for i, c in enumerate(cands)]
res.sort(reverse=True); mejor_ref = res[0][1]
print("mejor referencia:", os.path.basename(mejor_ref), f"{res[0][0]:.3f}")
# 2) ajustes sobre la mejor referencia
aj = []
for expr in (0.4, 0.55, 0.7):
    for cfg in (0.3, 0.6):
        s, out = probar(mejor_ref, expr, cfg, f"e{expr}_c{cfg}"); aj.append((s, expr, cfg, out))
aj.sort(reverse=True); s, expr, cfg, out = aj[0]
shutil.copy(mejor_ref, os.path.join(D, "ref_chatter.wav"))
json.dump({"expr": expr, "cfg": cfg, "parecido": s, "ref": os.path.basename(mejor_ref)}, open(os.path.join(D, "ajustes_chatter.json"), "w"))
shutil.copy(out, os.path.join(D, "mejor_muestra.wav"))
print(f"MEJOR: expr={expr} cfg={cfg} parecido={s:.3f}")
