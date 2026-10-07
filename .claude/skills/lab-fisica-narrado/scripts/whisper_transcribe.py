#!/usr/bin/env python3
"""Transcribe un WAV/MP3 con Whisper base (sherpa-onnx, local, int8) y escribe texto plano.
Uso: ~/.venvs/lab-fisica/bin/python whisper_transcribe.py audio.wav
Nota: esta build NO entrega timestamps; sirve para verificar que el audio dice el guion.
Si algún día HuggingFace está permitido, usa faster-whisper con word_timestamps=True."""
import os, sys, subprocess, tempfile, wave
import numpy as np, sherpa_onnx

M = os.path.expanduser("~/.local/share/whisper-models/sherpa-onnx-whisper-base")
src = sys.argv[1]
with tempfile.TemporaryDirectory() as td:
    wav = os.path.join(td, "a.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-ac", "1", "-ar", "16000", wav], check=True)
    w = wave.open(wav)
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
r = sherpa_onnx.OfflineRecognizer.from_whisper(
    encoder=f"{M}/base-encoder.int8.onnx", decoder=f"{M}/base-decoder.int8.onnx",
    tokens=f"{M}/base-tokens.txt", language="es", task="transcribe", num_threads=4)
s = r.create_stream(); s.accept_waveform(16000, x); r.decode_stream(s)
print(s.result.text.strip())
