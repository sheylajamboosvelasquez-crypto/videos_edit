#!/usr/bin/env python3
"""Escribe un JSON de props de Remotion por cada segmento de tipo tarjeta."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib
LAB = os.environ.get("LAB", "")
SEGMENTOS = importlib.import_module("segmentos_" + LAB if LAB else "segmentos").SEGMENTOS
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRAB = os.path.join(RAIZ, "salida", LAB, "trabajo") if LAB else os.path.join(RAIZ, "salida", "trabajo")
T = {t["id"]: t for t in json.load(open(os.path.join(TRAB, "tiempos.json")))}
os.makedirs(os.path.join(TRAB, "props"), exist_ok=True)
for s in SEGMENTOS:
    if s["visual"]["kind"] == "footage":
        continue
    t = T[s["id"]]
    json.dump(dict(visual=s["visual"], dur=t["dur"], cues=t["cues"]),
              open(os.path.join(TRAB, "props", f"{s['id']}.json"), "w"), ensure_ascii=False)
    print(s["id"], t["dur"])
