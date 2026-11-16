#!/usr/bin/env bash
cd /home/user/videos_edit
LAB=lab6 ~/.venvs/lab-fisica/bin/python -I -u proyecto/video.py v1 fondo > salida/lab6/trabajo/build_v1.log 2>&1
echo "exit=$?"; tail -3 salida/lab6/trabajo/build_v1.log; df -h / | tail -1
