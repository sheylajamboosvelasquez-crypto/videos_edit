#!/usr/bin/env python3
"""edge-tts con el CA del proxy del entorno (si existe). Uso:
tts_edge.py "texto" salida.mp3 [voz] [rate]   (voz por defecto es-CO-SalomeNeural)"""
import asyncio, os, ssl, sys
import edge_tts, edge_tts.communicate as c
CA = "/root/.ccr/ca-bundle.crt"
if os.path.exists(CA):
    c._SSL_CTX = ssl.create_default_context(cafile=CA)
text, out = sys.argv[1], sys.argv[2]
voice = sys.argv[3] if len(sys.argv) > 3 else "es-CO-SalomeNeural"
rate = sys.argv[4] if len(sys.argv) > 4 else "+0%"
asyncio.run(edge_tts.Communicate(text, voice, rate=rate, proxy=os.environ.get("HTTPS_PROXY")).save(out))
