# Guion v2: Circuitos resistivos y ley de Ohm (Experiencia N.º 4)

Fuente única de datos: informe *lab4.docx* (grupo 26253, Física de campos, CUC). No se agregó ningún dato que no esté en el informe.
Voz: es-CO-SalomeNeural (edge-tts) · ritmo ≈ 2,5 palabras/s · duración estimada total ≈ 9 min.

**Cómo leer este guion**
- **Pantalla**: lo que se ve (video crudo, tarjeta con ecuación, tabla, esquema).
- **Voz**: texto exacto que se narra. Los números van escritos como se pronuncian, para que la voz los lea bien. En pantalla aparecen en cifras.
- Los tiempos de los bloques 4 y 5 (montaje) se ajustarán al video crudo cuando lo tenga.
- `[CONFIRMAR: …]` marca algo que necesito que me confirmes.

---

## Bloque 0: Portada · 0:00–0:14 (≈ 14 s)
**Pantalla:** título "Circuitos resistivos y ley de Ohm, Experiencia N.º 4", integrantes, Física de campos, grupo 26253, docente Lic. Diana Delgado González, 07/10/26. Fondo: plano general del montaje (video crudo).
**Voz:** En este video presentamos la experiencia número cuatro de Física de campos: circuitos resistivos y ley de Ohm. Veremos el montaje, la teoría, los cálculos y el cuestionario resuelto.

## Bloque 1: Objetivos · 0:14–0:42 (≈ 28 s)
**Pantalla:** objetivo general y los cuatro específicos, apareciendo uno a uno.
**Voz:** El objetivo general es analizar experimentalmente la corriente, el voltaje y la resistencia equivalente en circuitos en serie y en paralelo, verificando la ley de Ohm. Para lograrlo, identificamos las resistencias con el código de colores y el óhmetro, calculamos y medimos la resistencia equivalente, comparamos corrientes y voltajes en cada elemento y explicamos el brillo de bombillas en distintos arreglos.

## Bloque 2: Marco teórico · 0:42–2:20 (≈ 98 s)
**2a. Ley de Ohm**
**Pantalla:** ecuación (1) I = V / R.
**Voz:** La ley de Ohm dice que la corriente en un conductor es directamente proporcional al voltaje entre sus extremos e inversamente proporcional a su resistencia. Los materiales que la cumplen se llaman óhmicos o lineales.

**2b. Serie**
**Pantalla:** esquema de tres resistencias en serie + ecuación (2) R_T = R1 + R2 + … + R_N.
**Voz:** En serie, las resistencias van una tras otra. La corriente es la misma en todas, el voltaje de la fuente se reparte entre ellas, y la resistencia equivalente es la suma de todas, siempre mayor que cualquiera de ellas.

**2c. Paralelo**
**Pantalla:** esquema en paralelo + ecuación (3) 1/R_T = 1/R1 + 1/R2 + … + 1/R_N.
**Voz:** En paralelo, todas las resistencias se conectan a los mismos dos puntos. El voltaje es igual en cada rama, la corriente total se divide, pasando más corriente por la rama de menor resistencia, y la equivalente es menor que la más pequeña.

**2d. Kirchhoff y potencia**
**Pantalla:** ecuación (4) P = V·I = I²R = V²/R.
**Voz:** Estas reglas salen de las leyes de Kirchhoff: en un lazo, las caídas de voltaje suman el voltaje de la fuente, y en un nodo, la corriente que entra es igual a la que sale. Además, una resistencia disipa potencia en forma de calor; en una bombilla, a mayor potencia, mayor brillo.

**2e. Código de colores y multímetro**
**Pantalla:** ecuación (5) Tol(Ω) = R_nominal × Tol(%) / 100; iconos de óhmetro, voltímetro en paralelo y amperímetro en serie.
**Voz:** Las resistencias comerciales traen un código de colores con su valor nominal y su tolerancia; la banda dorada indica más o menos cinco por ciento. Con el multímetro, la resistencia se mide sin energía, el voltaje en paralelo con el elemento, y la corriente con el instrumento en serie.

## Bloque 3: Materiales · 2:20–2:42 (≈ 22 s)
**Pantalla:** video crudo mostrando cada equipo, con rótulo de su nombre.
**Voz:** Usamos un multímetro Fluke ciento quince, el laboratorio electrónico EM ocho mil seiscientos cincuenta y seis de Pasco, la interfaz PASCO ochocientos cincuenta con el software Capstone y un sensor de voltaje, tres resistencias, una protoboard, una fuente de diez voltios y cables.

## Bloque 4: Montaje y procedimiento · 2:42–4:15 (≈ 93 s, se ajusta al video crudo)
**Pantalla:** video crudo, con rótulos de cada paso y zoom en las conexiones.
**4a. Reconocimiento:** Primero identificamos cada resistencia. R uno y R dos son de trescientos treinta ohmios y R tres de quinientos sesenta, todas con cinco por ciento de tolerancia. Las medimos con el óhmetro, siempre sin energía.
**4b. Serie:** Luego armamos el circuito en serie, con el cable rojo al mayor potencial y el negro al menor. Con la fuente desconectada medimos la resistencia equivalente. Después energizamos con diez voltios, medimos el voltaje en cada resistencia con el sensor de la interfaz, en paralelo, y la corriente del lazo con el multímetro como amperímetro, en serie.
**4c. Paralelo:** Después conectamos las tres resistencias entre los mismos dos nodos. Medimos la resistencia equivalente sin energía, y con la fuente encendida medimos el voltaje y la corriente de cada rama y la total.

## Bloque 5: Resultados medidos · 4:15–5:10 (≈ 55 s)
**Pantalla:** Tabla 1 → Tabla 2 → Tabla 3, resaltando la fila que se nombra.
**Voz (Tabla 1):** Las resistencias midieron trescientos veintiocho coma dos, trescientos veintiocho coma cero y quinientos cincuenta y cuatro coma cuatro ohmios, todas dentro de su tolerancia.
**Voz (Tabla 2):** En serie, la corriente fue la misma en todo el lazo, cero coma cero cero nueve amperios, y el voltaje se repartió: dos coma sesenta y seis voltios en R uno, dos coma setenta en R dos, y cuatro coma cincuenta y seis en R tres.
**Voz (Tabla 3):** En paralelo, cada rama recibió nueve coma noventa y cinco voltios, y la corriente se dividió: cero coma cero treinta y uno en R uno y R dos, y cero coma cero diecisiete amperios en R tres, la de mayor resistencia.

## Bloque 6: Cálculos con valores nominales · 5:10–6:25 (≈ 75 s)
**Pantalla:** cada ecuación aparece al narrarla (imágenes 06–18 del informe).
**6a. Serie:**
**Voz:** Con los valores nominales, la resistencia equivalente en serie es trescientos treinta, más trescientos treinta, más quinientos sesenta: mil doscientos veinte ohmios. La corriente es diez voltios entre mil doscientos veinte ohmios: cero coma cero cero ochenta y dos amperios. Así, R uno y R dos tienen dos coma setenta voltios cada una, y R tres cuatro coma cincuenta y nueve. Sumados dan diez voltios, el voltaje de la fuente. La potencia total es cero coma cero ochenta y dos vatios.
**6b. Paralelo:**
**Voz:** En paralelo, sumamos los inversos: uno entre trescientos treinta, dos veces, más uno entre quinientos sesenta, da cero coma cero cero siete ocho cuatro seis. Su inverso es ciento veintisiete coma cinco ohmios. Cada rama de trescientos treinta ohmios lleva cero coma cero trescientos tres amperios, y la de quinientos sesenta, cero coma cero ciento setenta y nueve. La corriente total es cero coma cero setecientos ochenta y cinco amperios, y la potencia, cero coma setecientos ochenta y cinco vatios.

## Bloque 7: Cálculos con valores medidos y errores · 6:25–7:35 (≈ 70 s)
**Pantalla:** ecuaciones 19–29 del informe + Tabla 4.
**Voz:** Con los valores medidos, la equivalente en serie es mil doscientos diez coma seis ohmios, y los voltajes suman nueve coma noventa y dos voltios, lo que confirma la ley de voltajes de Kirchhoff. En paralelo, las corrientes de rama suman cero coma cero setenta y nueve amperios, igual a la total medida, lo que confirma la ley de corrientes. El óhmetro marcó ciento veintiséis coma ocho ohmios.
Comparando con la teoría, el error fue de cero coma setenta y siete por ciento en serie y cero coma cincuenta y cinco por ciento en paralelo, dentro de la tolerancia. Por ley de Ohm, en serie el error subió a nueve coma sesenta y seis por ciento, porque la corriente medida, cero coma cero cero nueve amperios, es cerca de un diez por ciento mayor que la teórica; esto se atribuye a la lectura o a la escala del amperímetro. En paralelo, el error fue de uno coma veinticinco por ciento.

## Bloque 8: Cuestionario de la guía resuelto · 7:35–8:45 (≈ 70 s)
**[CONFIRMAR: el informe no trae las preguntas literales de la guía. Lo que sigue se basa en el análisis de las figuras a, b y c que está en el informe. Si la guía tiene más preguntas, envíamelas (texto o foto) y las agrego.]**
**Pantalla:** esquemas de las figuras a, b y c de la guía [CONFIRMAR: necesito la imagen de la guía o los redibujo como esquema simple], con la bombilla que se analiza resaltada.
**Figura a: dos bombillas en serie**
**Voz:** Figura a: dos bombillas en serie. Comparten un solo camino, así que cada una recibe la mitad del voltaje. Con la mitad del voltaje, disipa la cuarta parte de la potencia, y por eso brillan de forma tenue.
**Figura b: dos bombillas en paralelo**
**Voz:** Figura b: dos bombillas en paralelo. Cada una recibe el voltaje completo de la batería, de forma independiente, así que brillan con su máxima intensidad y por igual. Si una se desconecta, la otra sigue encendida.
**Figura c: arreglo mixto**
**Voz:** Figura c: L uno en serie con el bloque en paralelo de L dos y L tres. Ese bloque tiene la mitad de la resistencia de una bombilla, así que L uno se queda con dos tercios del voltaje y L dos y L tres con un tercio. Por eso L uno brilla más, y disipa cuatro veces la potencia de L dos o de L tres.

## Bloque 9: Conclusiones · 8:45–9:25 (≈ 40 s)
**Pantalla:** las cuatro conclusiones en viñetas, con los números clave resaltados; cierre sobre el montaje.
**Voz:** En conclusión, se validaron la ley de Ohm y las leyes de Kirchhoff. La resistencia equivalente en serie fue unas nueve coma cinco veces mayor que en paralelo. Las medidas con el óhmetro coincidieron con la teoría con errores menores al uno por ciento. Y la forma de conectar el circuito define el voltaje y la potencia de cada elemento: con los mismos diez voltios, el paralelo disipa casi diez veces más potencia que la serie.

---

## Decisiones que necesito de ti antes de generar el audio
1. ¿Apruebas este guion o qué cambias?
2. Formato final: 16:9 (horizontal) o 9:16 (vertical).
3. ¿Música de fondo? Solo si la pides, y tendrías que enviarme el archivo.
4. Cuestionario: ¿la guía tiene más preguntas además de las figuras a, b y c?
5. Video de referencia: desde aquí no puedo abrir YouTube. Si quieres algo concreto de su estilo (colores, tipografía, tarjetas, ritmo), descríbelo o envíame capturas.

---

# Plan de imágenes v2 (a partir del video crudo)

**Video crudo:** `crudo lab 4.mp4` · 6:40,9 · 1920×1080 · 30 fps. Es una recopilación de clips de celular:
- Clips **horizontales**: 0:04–0:08, 0:49–1:26, 2:27–2:54.
- Clips **verticales** (con barras negras): 0:00–0:04, 0:08–0:49, 1:26–2:27, 2:54–6:40.
- Audio original: ambiente de laboratorio muy bajo (−54 dB de promedio). Propuesta: quitarlo, o dejarlo al 5 % bajo la voz.

**Tratamiento visual propuesto (16:9, 1920×1080):**
- Los clips verticales van centrados, con fondo del mismo clip **desenfocado** en lugar de barras negras.
- Se estabilizan los clips más movidos (deshake) y se descartan los planos inútiles: batas, piso, cámara en movimiento.
- Las tarjetas de teoría, cálculos, tablas y cuestionario se hacen con **Remotion**: fondo oscuro, rojo institucional del logo CUC, tipografía Inter, y las ecuaciones del informe animadas paso a paso.
- Cada clip lleva un rótulo inferior pequeño con lo que se ve (por ejemplo, «Medición de voltaje con el multímetro Fluke 115»).

| Bloque | Duración | Imágenes |
|---|---|---|
| 0 Portada | 14 s | Foto de grupo 0:00–0:03 de fondo (desenfocada) + título en Remotion |
| 1 Objetivos | 28 s | Tarjeta Remotion sobre plano general de la placa 0:27–0:35 desenfocado |
| 2 Teoría | 98 s | Tarjetas Remotion: ecuaciones (1)–(5), esquemas serie y paralelo animados, iconos de medición |
| 3 Materiales | 22 s | Multímetro 0:50–0:53 · placa EM-8656 «Kit 4» 2:34–2:41 · interfaz PASCO 850 3:17–3:27 · Capstone 1:25 |
| 4 Montaje | ≈ 93 s | Resistencias y óhmetro 3:30–3:45 · cableado en la placa 2:27–2:31 y 2:44–2:51 · medición de voltaje 1:55–2:15 · lecturas del Fluke 2:52–3:10 y 4:40 · mediciones en la placa 3:57–4:35 · planos finales de la placa 6:32–6:40 |
| 5 Resultados | 55 s | Pantalla con la tabla en Excel 0:59–1:15 (con zoom) y luego las Tablas 1–3 rehechas en Remotion |
| 6 Cálculos nominales | 75 s | Ecuaciones 06–18 del informe, animadas una a una |
| 7 Cálculos medidos | 70 s | Ecuaciones 19–29 + Tabla 4 |
| 8 Cuestionario | 70 s | Esquemas a, b y c dibujados en Remotion, con el brillo de las bombillas animado |
| 9 Conclusiones | 40 s | Viñetas en Remotion; cierre con 6:07–6:12 (grupo) y créditos |

**Total estimado: ≈ 9 min 25 s.**

## Lo que necesito que confirmes
1. **Serie y paralelo en el video:** en los planos de la placa no distingo con seguridad cuál circuito es serie y cuál paralelo. Mientras no me lo confirmes, la narración del bloque 4 habla de «el montaje» sin decir cuál se ve en cada momento. Si sabes los minutos («serie de 1:55 a 2:15», «paralelo de 3:57 a 4:35»), lo afino.
2. **Personas:** en 5:47 aparece una persona que parece ser la docente. Por defecto **no la incluyo**. Las caras del grupo (0:00, 0:57, 6:07–6:30) sí las uso en portada y cierre. ¿Está bien así?
3. **Audio ambiente:** ¿lo quito o lo dejo muy bajo?
4. Siguen pendientes las preguntas del final de la v1: aprobación del guion, preguntas literales del cuestionario y las figuras a, b y c de la guía, y si quieres música.
