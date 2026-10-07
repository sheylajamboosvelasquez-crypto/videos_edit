#!/usr/bin/env python3
"""Escribe un JSON de props de Remotion por cada segmento de tipo tarjeta."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from segmentos import SEGMENTOS
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = {t["id"]: t for t in json.load(open(os.path.join(RAIZ, "salida/trabajo/tiempos.json")))}
os.makedirs(os.path.join(RAIZ, "salida/trabajo/props"), exist_ok=True)
for s in SEGMENTOS:
    if s["visual"]["kind"] == "footage":
        continue
    t = T[s["id"]]
    json.dump(dict(visual=s["visual"], dur=t["dur"], cues=t["cues"]),
              open(os.path.join(RAIZ, f"salida/trabajo/props/{s['id']}.json"), "w"), ensure_ascii=False)
    print(s["id"], t["dur"])
