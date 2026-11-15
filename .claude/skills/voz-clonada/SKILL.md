---
name: voz-clonada
description: Narrar con la voz clonada del usuario (XTTS-v2, local, sin pago). Úsalo cuando el usuario pida que el video o la narración salga con su propia voz, clonar su voz a partir de una grabación, o rehacer un audio con su voz en lugar de una voz de IA genérica.
---

# Voz clonada del usuario (XTTS-v2 o Chatterbox)

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
  --extra-index-url https://pypi.org/simple "torch==2.8.0" "torchaudio==2.8.0" "transformers>=4.57,<4.58"
uv pip install --python ~/.venvs/voz/bin/python coqui-tts soundfile six
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

## Motor alternativo: Chatterbox Multilingual (MIT, más expresivo)
Pone una marca de agua inaudible (Perth) en todo audio generado: **no se desactiva nunca**.
```bash
uv venv ~/.venvs/chatter --python 3.11
uv pip install --python ~/.venvs/chatter/bin/python --index-url https://download.pytorch.org/whl/cpu \
  --extra-index-url https://pypi.org/simple "torch==2.6.0" "torchaudio==2.6.0"
uv pip install --python ~/.venvs/chatter/bin/python chatterbox-tts "setuptools<81"
# referencia: un trozo continuo de 10-20 s del usuario hablando natural -> ~/.local/share/voz-usuario/ref_chatter.wav
~/.venvs/chatter/bin/python -I $SK/tts_chatter.py "texto" salida.wav --expr 0.6   # 0.5 normal, 0.7 más animado
```
Más lento que XTTS en CPU (~6 s de proceso por segundo de audio).

## Parecido y verificación (Chatterbox)
```bash
# busca entre tus grabaciones la referencia de 10 s y los ajustes (expr, cfg) que más se parecen a tu voz real;
# deja ref_chatter.wav y ajustes_chatter.json en ~/.local/share/voz-usuario (tts_chatter.py los usa solos)
~/.venvs/chatter/bin/python -I $SK/buscar_parecido.py
# --verificar: transcribe cada frase con Whisper y regenera las que no coinciden (hasta 3 intentos). Úsalo siempre para el video.
~/.venvs/chatter/bin/python -I $SK/tts_chatter.py --lote tramos.json --verificar
```
El parecido se mide con la huella de voz del modelo (1,0 = idéntica). Techo con las grabaciones actuales: 0,958
(tus dos grabaciones entre sí); una grabación con la grabadora del celular, sin compresión de WhatsApp, sube ese techo.

## Acabado «dulce»
`--dulce` suaviza los agudos, da algo de calidez y baja un 4 % la velocidad sin cambiar el tono. `ajustes_chatter.json`
admite `expr`, `cfg`, `temp`, `ref` (archivo dentro de voz-usuario) y `dulce: true` para fijar la voz elegida.

## Si suena robótica o monótona
1. Unir varias grabaciones: `preparar_voz.py grab1.ogg grab2.ogg` (más variedad de entonación).
2. XTTS: subir `--temp` (0.8-0.85). Chatterbox: subir `--expr` (0.6-0.75).
3. Escribir el guion con puntuación natural (comas, preguntas, exclamaciones): la entonación sale de ahí.

## Integración con lab-fisica-narrado
`proyecto/audio.py` usa la voz clonada con `VOZ=clon`:
```bash
VOZ=clon COQUI_TOS_AGREED=1 ~/.venvs/lab-fisica/bin/python -I proyecto/audio.py
```
El resto del flujo (tiempos, tarjetas, subtítulos, armado) no cambia.

## Pronunciación
- Escribir los números en palabras (como en lab-fisica-narrado).
- XTTS puede leer «Ohm» a la inglesa: si suena raro, escribir «Om» en el texto narrado (el subtítulo sigue diciendo Ohm).
- Velocidad en CPU: ~2 s de proceso por cada segundo de audio (8 min de narración ≈ 15-20 min).

## Consejos para la grabación del usuario
- 1 a 3 minutos, habitación callada, celular a 15-20 cm, tono natural (como va a sonar el video).
- Leer texto con números, términos técnicos, una pregunta y una exclamación.
- Si la voz clonada suena rara: pedir una grabación más larga o más limpia (sin eco ni ruido) y repetir el paso 1.
