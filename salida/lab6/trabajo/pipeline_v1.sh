#!/usr/bin/env bash
# narración (reanuda: salta los tramos ya hechos) -> props -> armado con fondo
cd /home/user/videos_edit
LAB=lab6 VOZ=chatter ~/.venvs/lab-fisica/bin/python -I -u proyecto/audio.py >> salida/lab6/trabajo/audio_v1.log 2>&1 || { echo "FALLO AUDIO"; exit 1; }
grep -q TOTAL salida/lab6/trabajo/audio_v1.log || { echo "AUDIO SIN TOTAL"; exit 1; }
LAB=lab6 python3 -I proyecto/props.py > /dev/null
LAB=lab6 ~/.venvs/lab-fisica/bin/python -I -u proyecto/video.py v1 fondo > salida/lab6/trabajo/build_v1.log 2>&1
echo "exit=$?"; tail -3 salida/lab6/trabajo/build_v1.log
