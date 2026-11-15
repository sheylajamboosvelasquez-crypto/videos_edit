#!/usr/bin/env python3
"""Narración con la voz clonada usando Chatterbox Multilingual (Resemble AI, licencia MIT), CPU.
Más expresivo que XTTS: `--expr` controla la entonación (0.5 normal, 0.7 más animado).
Uso:
  tts_chatter.py "texto" salida.wav [--ref ref.wav] [--expr 0.6] [--cfg 0.4]
  tts_chatter.py --lote tramos.json   # [{"texto": ..., "salida": ...}, ...]
La referencia es un solo audio de 10-20 s del usuario hablando natural (por defecto ref_chatter.wav)."""
import argparse, json, os, re, time
import torch, torchaudio

ap = argparse.ArgumentParser()
ap.add_argument("texto", nargs="?"); ap.add_argument("salida", nargs="?"); ap.add_argument("--lote")
ap.add_argument("--ref", default="~/.local/share/voz-usuario/ref_chatter.wav")
ap.add_argument("--expr", type=float, default=0.6); ap.add_argument("--cfg", type=float, default=0.4)
a = ap.parse_args()
torch.set_num_threads(os.cpu_count() or 4)
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
t0 = time.time()
m = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
print(f"modelo cargado en {time.time() - t0:.0f} s", flush=True)
ref = os.path.expanduser(a.ref)


def frases(t, maxc=220):
    partes, cur = [], ""
    for f in re.split(r"(?<=[.!?¿¡;:])\s+", t.strip()):
        if cur and len(cur) + len(f) > maxc:
            partes.append(cur); cur = f
        else:
            cur = (cur + " " + f).strip()
    return partes + ([cur] if cur else [])


trabajos = json.load(open(a.lote)) if a.lote else [{"texto": a.texto, "salida": a.salida}]
for t in trabajos:
    t1, trozos = time.time(), []
    for f in frases(t["texto"]):
        w = m.generate(f, language_id="es", audio_prompt_path=ref, exaggeration=a.expr, cfg_weight=a.cfg)
        trozos += [w, torch.zeros(1, int(m.sr * 0.18))]  # pausa breve entre frases
    torchaudio.save(t["salida"], torch.cat(trozos[:-1], dim=1), m.sr)
    print(f"listo {t['salida']} ({time.time() - t1:.0f} s)", flush=True)
