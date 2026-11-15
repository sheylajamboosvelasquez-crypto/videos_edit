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
ap.add_argument("--temp", type=float, default=0.8, help="variedad de la generación (0.8 normal, 1.0 más variada)")
ap.add_argument("--dulce", action="store_true", help="acabado suave: +calidez en 250 Hz, -3 dB en agudos y 4 %% más pausado")
ap.add_argument("--verificar", action="store_true", help="transcribe cada frase con Whisper y regenera si no coincide (hasta 3 intentos)")
a = ap.parse_args()
# ajustes que encontró buscar_parecido.py (si existen) mandan sobre los valores por defecto
_aj = os.path.expanduser("~/.local/share/voz-usuario/ajustes_chatter.json")
if os.path.exists(_aj) and "--expr" not in os.sys.argv and "--cfg" not in os.sys.argv:
    _j = json.load(open(_aj)); a.expr, a.cfg = _j["expr"], _j["cfg"]
    if "temp" in _j and "--temp" not in os.sys.argv: a.temp = _j["temp"]
    if "ref" in _j and "--ref" not in os.sys.argv: a.ref = os.path.join(os.path.dirname(_aj), _j["ref"])
    if _j.get("dulce"): a.dulce = True
torch.set_num_threads(os.cpu_count() or 4)
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
t0 = time.time()
m = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
print(f"modelo cargado en {time.time() - t0:.0f} s", flush=True)
ref = os.path.expanduser(a.ref)


def frases(t, maxc=140):
    partes, cur = [], ""
    for f in re.split(r"(?<=[.!?¿¡;:])\s+", t.strip()):
        if cur and len(cur) + len(f) > maxc:
            partes.append(cur); cur = f
        else:
            cur = (cur + " " + f).strip()
    return partes + ([cur] if cur else [])


# --- verificación con Whisper base (sherpa-onnx, local): compara lo dicho con lo pedido ---
import difflib, unicodedata
rec = None
if a.verificar:
    import numpy as np, sherpa_onnx
    M = os.path.expanduser("~/.local/share/whisper-models/sherpa-onnx-whisper-base")
    rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=f"{M}/base-encoder.int8.onnx", decoder=f"{M}/base-decoder.int8.onnx",
                                                     tokens=f"{M}/base-tokens.txt", language="es", task="transcribe", num_threads=2)

def norm(t):
    t = unicodedata.normalize("NFD", t.lower()); t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9ñ ]+", " ", t).split()

def puntaje(wav, texto):
    x = torchaudio.functional.resample(wav, m.sr, 16000)[0].numpy().astype("float32")
    st = rec.create_stream(); st.accept_waveform(16000, x); rec.decode_stream(st)
    return difflib.SequenceMatcher(None, norm(texto), norm(st.result.text)).ratio(), st.result.text

def generar(f):
    mejor = None
    for intento in range(3 if rec else 1):
        w = m.generate(f, language_id="es", audio_prompt_path=ref, exaggeration=a.expr, cfg_weight=a.cfg, temperature=a.temp)
        if not rec:
            return w
        sc, oido = puntaje(w, f)
        if mejor is None or sc > mejor[0]:
            mejor = (sc, w)
        if sc >= 0.78:
            break
        print(f"   reintento {intento + 1}: coincidencia {sc:.2f} -> «{oido.strip()}»", flush=True)
    return mejor[1]

trabajos = json.load(open(a.lote)) if a.lote else [{"texto": a.texto, "salida": a.salida}]
for t in trabajos:
    t1, trozos = time.time(), []
    for f in frases(t["texto"]):
        w = generar(f)
        trozos += [w, torch.zeros(1, int(m.sr * 0.18))]  # pausa breve entre frases
    torchaudio.save(t["salida"], torch.cat(trozos[:-1], dim=1), m.sr)
    if a.dulce:
        import subprocess
        tmp = t["salida"] + ".tmp.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", t["salida"], "-af",
                        "atempo=0.96,equalizer=f=250:t=q:w=1.2:g=2,highshelf=f=5500:g=-3", tmp], check=True)
        os.replace(tmp, t["salida"])
    print(f"listo {t['salida']} ({time.time() - t1:.0f} s)", flush=True)
