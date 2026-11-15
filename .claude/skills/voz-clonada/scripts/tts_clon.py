#!/usr/bin/env python3
"""Narración con la voz clonada del usuario (XTTS-v2, local, CPU).
Uso:
  tts_clon.py "texto" salida.wav                  # una frase
  tts_clon.py --lote tramos.json                  # [{"texto": ..., "salida": ...}, ...] (carga el modelo una vez)
Opciones: --refs DIR (por defecto ~/.local/share/voz-usuario), --vel 1.0 (velocidad), --temp 0.6
Modelo coqui/XTTS-v2: licencia CPML (uso no comercial). Requiere COQUI_TOS_AGREED=1."""
import argparse, glob, json, os, sys, time

ap = argparse.ArgumentParser()
ap.add_argument("texto", nargs="?"); ap.add_argument("salida", nargs="?")
ap.add_argument("--lote"); ap.add_argument("--refs", default="~/.local/share/voz-usuario")
ap.add_argument("--vel", type=float, default=1.0); ap.add_argument("--temp", type=float, default=0.6)
a = ap.parse_args()
os.environ.setdefault("COQUI_TOS_AGREED", "1")
refs = sorted(glob.glob(os.path.join(os.path.expanduser(a.refs), "ref_*.wav")))
if not refs:
    sys.exit("No hay referencias: corre primero preparar_voz.py con la grabación del usuario.")

import torch
from TTS.api import TTS
torch.set_num_threads(os.cpu_count() or 4)
t0 = time.time()
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False).to("cpu")
print(f"modelo cargado en {time.time() - t0:.0f} s; referencias: {len(refs)}", flush=True)

trabajos = json.load(open(a.lote)) if a.lote else [{"texto": a.texto, "salida": a.salida}]
for t in trabajos:
    t1 = time.time()
    tts.tts_to_file(text=t["texto"], speaker_wav=refs, language="es", file_path=t["salida"],
                    speed=a.vel, temperature=a.temp, split_sentences=True)
    print(f"listo {t['salida']} ({time.time() - t1:.0f} s)", flush=True)
