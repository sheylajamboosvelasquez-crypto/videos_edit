---
name: voz-clonada
description: Narrar con la voz clonada del usuario (XTTS-v2, local, sin pago). Úsalo cuando el usuario pida que el video o la narración salga con su propia voz, clonar su voz a partir de una grabación, o rehacer un audio con su voz en lugar de una voz de IA genérica.
---

# Voz clonada del usuario (XTTS-v2)

Clona la voz del usuario a partir de una grabación suya de 1 a 3 minutos y genera la narración con esa voz.
Funciona sin internet una vez descargado el modelo y sin tarjeta gráfica (más lento en CPU).

## Reglas
1. **Solo la voz del propio usuario**, con su permiso explícito. Nunca clonar la voz de otra persona
   (compañeros, docentes, famosos) aunque se pida, salvo que esa persona dé su consentimiento directo.
2. **La grabación es privada.** Va en `~/.local/share/voz-usuario/` (permiso 600) y **nunca** se sube a GitHub
   ni a ningún servicio externo.
3. **Licencia del modelo:** coqui/XTTS-v2 usa la licencia CPML (Coqui Public Model License), **solo uso no comercial**
   (una tarea de la universidad está bien; vender el video no). El usuario debe aceptarla: no la aceptes en su nombre.
   Cuando la acepte, se ejecuta con `COQUI_TOS_AGREED=1`.
4. Avisar que el resultado es una aproximación: puede sonar algo plano o tener pequeños errores de pronunciación.
   Escuchar una prueba antes de generar todo el video.

## Instalación (una vez por contenedor)
```bash
uv venv ~/.venvs/voz --python 3.12
uv pip install --python ~/.venvs/voz/bin/python --index-url https://download.pytorch.org/whl/cpu \
  --extra-index-url https://pypi.org/simple "torch==2.5.1" "torchaudio==2.5.1"
uv pip install --python ~/.venvs/voz/bin/python coqui-tts soundfile
```
Requiere acceso a `huggingface.co` (descarga del modelo, ~1,9 GB la primera vez).

## Uso
```bash
V=~/.venvs/voz/bin/python; SK=.claude/skills/voz-clonada/scripts
# 1. Preparar la grabación (WhatsApp .ogg, .m4a, .mp3 o .wav): limpia, normaliza y parte por pausas
$V -I $SK/preparar_voz.py GRABACION
# 2. Prueba corta (el usuario la escucha y aprueba)
COQUI_TOS_AGREED=1 $V -I $SK/tts_clon.py "Frase de prueba con números: diez voltios, cero coma cero cero ochenta y dos amperios." prueba.wav
# 3. Todos los tramos del video (carga el modelo una sola vez)
COQUI_TOS_AGREED=1 $V -I $SK/tts_clon.py --lote tramos.json      # [{"texto": "...", "salida": "...wav"}, ...]
```
Opciones: `--vel 1.05` (un poco más rápido), `--temp 0.5` (más estable, menos expresiva).

## Integración con lab-fisica-narrado
`proyecto/audio.py` usa la voz clonada con `VOZ=clon`:
```bash
VOZ=clon COQUI_TOS_AGREED=1 ~/.venvs/lab-fisica/bin/python -I proyecto/audio.py
```
El resto del flujo (tiempos, tarjetas, subtítulos, armado) no cambia.

## Consejos para la grabación del usuario
- 1 a 3 minutos, habitación callada, celular a 15-20 cm, tono natural (como va a sonar el video).
- Leer texto con números, términos técnicos, una pregunta y una exclamación.
- Si la voz clonada suena rara: pedir una grabación más larga o más limpia (sin eco ni ruido) y repetir el paso 1.
