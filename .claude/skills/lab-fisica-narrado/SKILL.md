---
name: lab-fisica-narrado
description: Narrar o agregar voz de IA en español a un video de laboratorio de física. Úsalo cuando el usuario pida narrar un video, agregar voz de IA, generar guion de laboratorio, subtítulos sincronizados o exportar el resultado (16:9 o 9:16). Cubre inspección con ffprobe, guion con tiempos, TTS (edge-tts o Piper), atempo, mezcla con loudnorm, subtítulos quemados y verificación.
---

# Laboratorio de física con narración de voz de IA

## Herramientas y rutas
- Entorno Python (no usar el Python del sistema): `~/.venvs/lab-fisica/bin/`
  - `edge-tts` (voz principal, **requiere internet** a speech.platform.bing.com)
  - `piper` (local, sin internet). Voz: `~/.local/share/piper-voices/es-carlfm-x-low.onnx` (calidad baja, 16 kHz)
  - Whisper base (sherpa-onnx, local): `scripts/whisper_transcribe.py` de este skill. **No da timestamps.**
- ffmpeg/ffprobe del sistema (filtros verificados: loudnorm, atempo, subtitles/libass, xfade, drawtext, sidechaincompress, amix).
- Fuente de subtítulos: **Inter** (`FontName=Inter`).
- Skills hermanos: `ffmpeg-skill` (cortes, exportes, doctor) y `remotion-*` (títulos y gráficos animados).

## Reglas (siempre)
1. **Nunca sobrescribir el original.** Todo va en `salida/` con nombres versionados: `salida/<nombre>_v1.mp4`, `_v2`, …
2. **No inventar datos científicos.** Valores, unidades, fórmulas y nombres solo si salen del video o de lo que diga el usuario. Si falta un dato, preguntar.
3. **Preguntar antes de cambiar el sentido** de algo (reordenar pasos, cambiar una conclusión, corregir un valor).
4. **Mostrar al usuario los comandos ejecutados** (lista breve al final de cada etapa).
5. Intermedios en `salida/trabajo/` (fotogramas, audios por tramo, SRT). No borrar sin avisar.
6. Detenerse y esperar aprobación en el paso 2 (guion).

## Flujo

### 1. Inspeccionar
```bash
mkdir -p salida/trabajo/frames
ffprobe -v error -show_entries format=duration:stream=index,codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels -of json VIDEO
ffmpeg -v error -i VIDEO -vf "fps=1/2.5,scale=960:-2" salida/trabajo/frames/f_%03d.jpg   # un fotograma cada 2–3 s
```
Ver los fotogramas (Read) para entender el montaje, los instrumentos, lo que se mide y lo que pasa en cada tramo. El fotograma `f_N` ≈ segundo `(N-1)*2.5`. Si el video ya trae audio, avisar y preguntar si se reemplaza, se baja de volumen o se conserva.

### 2. Guion por tramos (y PARAR)
- Escribir en español, por tramos con tiempos: `[mm:ss–mm:ss] texto`.
- Presupuesto: **≈ 2,5 palabras por segundo** (tramo de 8 s ≈ 20 palabras). Dejar ~0,3 s de aire entre tramos.
- Solo describir lo que se ve o lo que el usuario confirmó. Marcar dudas con `[CONFIRMAR: …]`.
- Guardar como `salida/trabajo/guion_v1.md` y **esperar aprobación explícita** antes de generar audio.

### 3. Audio por tramo
Voz por defecto **es-CO-SalomeNeural** (alternativa masculina: es-CO-GonzaloNeural).
```bash
V=~/.venvs/lab-fisica/bin
# En la nube (proxy con CA propio) usa el envoltorio, que fija el certificado correcto:
$V/python -I ~/.claude/skills/lab-fisica-narrado/scripts/tts_edge.py "TEXTO" salida/trabajo/t01.mp3 [voz] [rate]
# En una máquina normal también sirve directo:
$V/edge-tts --voice es-CO-SalomeNeural --text "TEXTO" --write-media salida/trabajo/t01.mp3
# Sin internet o si edge-tts falla (SkewAdjustmentError / 403): Piper
echo "TEXTO" | $V/piper -m ~/.local/share/piper-voices/es-carlfm-x-low.onnx -f salida/trabajo/t01.wav
ffprobe -v error -show_entries format=duration -of csv=p=0 salida/trabajo/t01.mp3   # duración real
```
Si cambia el motor/voz, avisar: el timbre cambia entre tramos.

### 4. Ajustar duraciones (atempo ≤ 1.15)
Comparar duración real con el tramo disponible. Si el audio es más largo:
- `factor = dur_audio / dur_tramo`; si `factor ≤ 1.15` → `ffmpeg -i t01.mp3 -filter:a "atempo=FACTOR" t01_a.wav`
- Si `factor > 1.15` → **no acelerar más**: acortar el texto del guion (volver a pedir aprobación si cambia el sentido) o ampliar el tramo/congelar un fotograma con ffmpeg-skill.
- Nunca recortar el audio con `-t`: comprobar que la última palabra no se corte (duración final ≤ tramo).

### 5. Montaje, loudnorm y música
```bash
# cada tramo en su instante exacto (ms), sin normalización automática de amix
ffmpeg -y -i t01.wav -i t02.wav ... \
  -filter_complex "[0]adelay=INICIO1_ms|INICIO1_ms[a0];[1]adelay=INICIO2_ms|INICIO2_ms[a1];[a0][a1]amix=inputs=N:normalize=0:dropout_transition=0,loudnorm=I=-16:TP=-1.5:LRA=11[voz]" \
  -map "[voz]" -ar 48000 salida/trabajo/voz_v1.wav
```
Música **solo si el usuario la pide**: voz como sidechain, p. ej. `[musica][voz]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=400[duck]` y luego `amix`. Pedir el archivo de música y confirmar su licencia; no descargar música por cuenta propia.

### 6. Subtítulos sincronizados
- Los tiempos salen del **montaje real** (inicio del tramo + duración medida con ffprobe): partir cada tramo en líneas de ≤ 42 caracteres y repartir el tiempo por palabras. Esto da sincronía exacta con el audio generado.
- Whisper se usa para **verificar** que el audio dice el guion: `~/.venvs/lab-fisica/bin/python ~/.claude/skills/lab-fisica-narrado/scripts/whisper_transcribe.py salida/trabajo/voz_v1.wav` (comparar con el guion; el modelo base puede errar en términos técnicos, no corregir el guion por eso). Con faster-whisper + `word_timestamps=True` (si HuggingFace está accesible) se pueden obtener tiempos por palabra.
- Escribir `salida/trabajo/subs_v1.srt` y quemarlos:
```bash
ffmpeg -y -i VIDEO -i salida/trabajo/voz_v1.wav -map 0:v -map 1:a \
  -vf "subtitles=salida/trabajo/subs_v1.srt:force_style='FontName=Inter,FontSize=22,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,BorderStyle=1,Outline=2,Alignment=2,MarginV=40'" \
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart salida/NOMBRE_v1.mp4
```
(Ajustar `FontSize` a la resolución; en 9:16 usar `MarginV` mayor para no tapar controles de la app.)

### 7. Exportar y verificar
- **16:9**: 1920×1080. **9:16**: 1080×1920 (`scale`+`pad` o recorte; preguntar cuál si el encuadre pierde información del experimento).
- H.264 + AAC, `yuv420p`, `+faststart`.
- Verificar:
```bash
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,duration -show_entries format=duration -of default=nw=1 salida/NOMBRE_v1.mp4
```
Duración de audio y de video con diferencia < 0,1 s; la última palabra del último tramo termina antes del final del video. Opcional: `npx ffmpeg-skill doctor` y las verificaciones de ffmpeg-skill.
- Entregar: ruta del archivo, resumen de comandos ejecutados y lista de supuestos/dudas.

## Plantilla de proyecto
El proyecto del Lab 4 (repo videos_edit, carpeta `proyecto/`) sirve de plantilla: `segmentos.py` (texto + visual por tramo), `audio.py` (voz y tiempos), `props.py` + `remotion/` (tarjetas animadas) y `video.py` (clips, unión, voz con loudnorm, subtítulos quemados).

## Límites conocidos de este entorno
- En el entorno en la nube, `speech.platform.bing.com` (edge-tts) y `huggingface.co` pueden estar bloqueados por la política de red; Piper y Whisper base funcionan sin internet.
- La voz Piper instalada es de baja calidad (x-low); edge-tts suena mucho mejor.
