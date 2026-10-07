#!/usr/bin/env bash
# Reinstala las herramientas de este proyecto en un contenedor nuevo (Ubuntu).
# Uso: bash proyecto/instalar_entorno.sh
set -euo pipefail
command -v uv >/dev/null || pip install uv
uv venv ~/.venvs/lab-fisica --python 3.13
uv pip install --python ~/.venvs/lab-fisica/bin/python edge-tts piper-tts sherpa-onnx soundfile gdown yt-dlp
# voz Piper (sin internet) y Whisper base (ONNX), ambos desde GitHub
mkdir -p ~/.local/share/piper-voices ~/.local/share/whisper-models
curl -sSL https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-es-carlfm-x-low.tar.gz | tar xz -C ~/.local/share/piper-voices
curl -sSL https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-base.tar.bz2 | tar xj -C ~/.local/share/whisper-models
# skills: ffmpeg-skill, Remotion y el skill propio del repo
npx --yes ffmpeg-skill
npx --yes skills add remotion-dev/skills -g -a claude-code -y
mkdir -p ~/.claude/skills && cp -r "$(dirname "$0")/../.claude/skills/lab-fisica-narrado" ~/.claude/skills/
(cd "$(dirname "$0")/remotion" && npm install --no-audit --no-fund)
echo "Listo. Abre una sesión nueva de Claude Code para que cargue los skills."
