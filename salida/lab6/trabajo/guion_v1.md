# Guion v1: Bobina de Helmholtz, campo magnético de una bobina circular (Experiencia N.º 6)

Fuente única de datos: informe *Informe_Experiencia_6_Bobina_de_Helmholtz.docx* (grupo 26253, Física de campos, CUC). No se agregó ningún dato que no esté en el informe.
Voz: la tuya, clonada (Chatterbox). v1.1: las fórmulas se narran en palabras, sin letras sueltas ni «mu cero», porque la voz clonada no las pronuncia bien · ritmo ≈ 2,5 palabras/s · duración estimada ≈ 9 min.

**Cómo leer este guion**
- **Pantalla**: lo que se ve. Igual que en la v2 del Lab 4: ustedes de fondo casi todo el tiempo y las tarjetas (ecuaciones, tablas, figuras) en un recuadro.
- **Voz**: texto exacto que se narra. Los números van escritos como se pronuncian; en pantalla aparecen en cifras.
- Los tiempos del bloque 4 (montaje) se ajustan al video crudo cuando lo tenga.
- `[CONFIRMAR: …]` marca algo que necesito que me confirmes.

---

## Bloque 0: Portada · ≈ 14 s
**Pantalla:** título «Bobina de Helmholtz: campo magnético de una bobina circular, Experiencia N.º 6», integrantes, Física de campos, grupo 26253, docente Lic. Diana Delgado González, 15/11/26. Fondo: video del grupo.
**Voz:** En este video presentamos la experiencia número seis de Física de campos: la bobina de Helmholtz y el campo magnético de una bobina circular. Veremos el montaje, la teoría, los resultados, los cálculos y las conclusiones.

## Bloque 1: Objetivos · ≈ 30 s
**Pantalla:** objetivo general y los cuatro específicos, apareciendo uno a uno.
**Voz:** El objetivo general es analizar cómo se distribuye en el espacio la intensidad del campo magnético que genera una bobina de Helmholtz. Para lograrlo, medimos las componentes axial y perpendicular del campo a lo largo del eje de una bobina circular, comparamos la curva experimental con el ajuste del programa y con el modelo teórico, calculamos el valor experimental de la permeabilidad del vacío con su porcentaje de error, y comparamos el perfil de una sola bobina con el que se espera para el par de Helmholtz.

## Bloque 2: Marco teórico · ≈ 100 s
**2a. Biot-Savart y el campo en el eje**
**Pantalla:** esquema de una espira con un punto sobre el eje; luego ecuación (1).
**Voz:** El campo magnético lo producen las cargas en movimiento, y su unidad es el tesla. La ley de Biot-Savart dice que cada pedacito de corriente aporta un campo que disminuye con el cuadrado de la distancia. Sobre el eje de una bobina circular el cálculo se simplifica: las componentes perpendiculares se cancelan por pares y solo queda la componente axial. Para una bobina con cierto número de espiras y cierto radio, el campo a una distancia del centro es la permeabilidad del vacío, por el número de espiras, por la corriente, por el radio al cuadrado, dividido entre dos veces, la distancia al cuadrado más el radio al cuadrado, elevado a tres medios.

**2b. Campo en el centro y permeabilidad**
**Pantalla:** ecuaciones (2) y (3); el valor μ₀ = 4π × 10⁻⁷ ≈ 1,257 × 10⁻⁶ T·m/A.
**Voz:** El campo es máximo en el centro de la bobina, y lejos de ella decae como uno sobre la distancia al cubo, igual que un dipolo magnético. En el centro, la ecuación se reduce a la permeabilidad, por el número de espiras, por la corriente, dividido entre dos veces el radio. Y de ahí despejamos la permeabilidad magnética del vacío: es igual a dos veces el radio por el campo en el centro, dividido entre el número de espiras por la corriente. Su valor de referencia es uno coma doscientos cincuenta y siete por diez a la menos seis teslas metro por amperio.

**2c. Componente perpendicular, par de Helmholtz y error**
**Pantalla:** ecuación (4); esquema de dos bobinas separadas una distancia R + ecuación (5); ecuación (6).
**Voz:** Por simetría, la componente perpendicular del campo debería ser cero sobre el eje. Si el sensor queda inclinado un pequeño ángulo, registra una parte del campo axial en el canal perpendicular, y ese ángulo se estima con el arcotangente del cociente entre las dos componentes. En el arreglo de Helmholtz, dos bobinas iguales separadas una distancia igual a su radio producen en el punto medio un campo casi uniforme, que vale cuatro quintos elevado a tres medios, por la permeabilidad, por el número de espiras, por la corriente, dividido entre el radio. Y para comparar con la referencia usamos el error relativo porcentual.

## Bloque 3: Materiales · ≈ 22 s
**Pantalla:** video crudo mostrando cada equipo, con rótulo.
**Voz:** Usamos una bobina circular de quinientas espiras y diez coma cero seis centímetros de radio, un sensor de campo magnético de dos ejes, axial y perpendicular, la interfaz PASCO ochocientos cincuenta con el software Capstone, y una pista con soportes para desplazar el sensor a lo largo del eje de la bobina.

## Bloque 4: Montaje y procedimiento · ≈ 95 s (se ajusta al video crudo)
**Pantalla:** video crudo, con rótulos de cada paso.
**4a. Conexión y cero del sensor:** Primero conectamos la bobina, el sensor de campo y la interfaz según el montaje de la guía. Deslizamos el sensor por la pista hasta que la sonda quedó en el centro de la bobina, y presionamos el botón TARE para poner el sensor en cero.
**4b. Corriente y toma de datos:** En el generador de señales de Capstone verificamos que el voltaje de corriente continua estuviera en seis coma dos voltios y lo encendimos; la interfaz registró una corriente de cero coma trescientos cuarenta y un amperios. Pulsamos vista previa, esperamos a que la medida se estabilizara y pulsamos mantener muestra, registrando las dos componentes del campo a diez hercios.
**4c. Barrido y ajuste:** Repetimos la medición desplazando el sensor de tres en tres centímetros, desde cero hasta veinticuatro centímetros, para un total de nueve datos. A los datos del campo axial les aplicamos un ajuste de curva definido por el usuario, con la forma de la ecuación uno.
**4d. Tres corrientes:** Por último, con el sensor en el centro, registramos el campo para tres corrientes: cero coma trescientos veintinueve, cero coma trescientos cincuenta y seis y cero coma trescientos ochenta y tres amperios, para calcular la permeabilidad del vacío y su error.

## Bloque 5: Resultados: perfil del campo · ≈ 75 s
**Pantalla:** Tabla 1 resaltando filas; luego Figura 1 (Capstone) y Figura 3 (comparación).
**Voz (Tabla 1):** El campo axial fue máximo en el centro, cerca de nueve coma ochenta y seis por diez a la menos cuatro teslas, y fue cayendo con la distancia: a tres centímetros conservaba cerca del ochenta y cinco por ciento de su valor, a quince centímetros solo el dieciséis por ciento, y a veintiún y veinticuatro centímetros quedó en valores del orden de diez a la menos seis teslas.
**Voz (Figura 1):** La curva tiene la forma de campana que predice la ecuación uno. El ajuste definido por el usuario siguió esa tendencia con un error cuadrático medio de cuatro coma cero nueve por diez a la menos cinco teslas, y dio un radio de nueve coma cincuenta y siete centímetros, frente a los diez coma cero seis medidos. Los parámetros del ajuste no se pueden interpretar por separado, porque el programa los reparte como quiere; solo tiene sentido su producto.
**Voz (Figura 3):** Frente a la curva teórica, los datos quedan por debajo en casi todo el recorrido, y en el centro el campo medido es siete coma cuatro por ciento menor que el teórico.

## Bloque 6: Resultados: componente perpendicular · ≈ 35 s
**Pantalla:** Figura 2 y ecuación (4) con los valores.
**Voz:** La componente perpendicular debería ser cero sobre el eje, pero en el centro el sensor registró nueve coma diecisiete por diez a la menos cinco teslas, y esa lectura bajó junto con el campo axial. Eso indica que el sensor estaba inclinado respecto al eje: con el arcotangente de cero coma cero noventa y tres, el ángulo es de unos cinco grados. Desde dieciocho centímetros la componente se volvió negativa, por el campo terrestre, que el TARE solo compensa en el punto donde se presionó, y por la deriva del cero del sensor.

## Bloque 7: Cálculo de μ₀ y error · ≈ 80 s
**Pantalla:** Tabla 3 → ecuación (7) → ecuación (8) → Tabla 4 → Figura 4.
**Voz:** Con el campo en el centro para cada corriente calculamos la permeabilidad. Para la primera, con radio de cero coma mil seis metros, campo de nueve coma cuarenta y nueve por diez a la menos cuatro teslas, quinientas espiras y cero coma trescientos veintinueve amperios, la permeabilidad da uno coma mil seiscientos siete por diez a la menos seis teslas metro por amperio. Su error frente al valor de referencia es de siete coma sesenta y seis por ciento. Para las otras dos corrientes los errores fueron de siete coma treinta y ocho y ocho coma cero seis por ciento, y el promedio de la permeabilidad fue uno coma ciento sesenta por diez a la menos seis.
Además, el campo en el centro creció en proporción a la corriente: la recta de ajuste por el origen tiene una pendiente de dos coma ochocientos ochenta y tres militeslas por amperio, frente a tres coma ciento veintitrés de la recta teórica, y de esa pendiente sale la misma permeabilidad, con siete coma siete por ciento de error.

## Bloque 8: Análisis: por qué el error y el par de Helmholtz · ≈ 70 s
**Pantalla:** viñetas con las causas; luego Figura 5 con la meseta resaltada.
**Voz:** Los tres errores difieren entre sí menos de un punto porcentual, así que la causa es sistemática: algo redujo el campo medido de la misma forma en todas las pruebas. La más probable es la posición de la sonda, porque un desplazamiento de dos centímetros respecto al centro reduce el campo en cinco coma siete por ciento. También influyen el radio efectivo del devanado, la inclinación del sensor y la calibración del sensor y del medidor de corriente.
Por último, comparamos el perfil de una bobina con el par de Helmholtz. Una sola bobina produce un pico en el centro, y a cinco centímetros ya perdió cerca del veintiocho por ciento. Con dos bobinas separadas una distancia igual al radio, el campo en el punto medio es uno coma cuarenta y tres veces mayor, unos uno coma cincuenta y dos militeslas, y forma una meseta que varía menos del cero coma cinco por ciento en más menos dos coma cinco centímetros. Por esa región casi uniforme, el arreglo se usa para generar campos de referencia.

## Bloque 9: Conclusiones · ≈ 45 s
**Pantalla:** tres conclusiones en viñetas; cierre con el grupo.
**Voz:** En conclusión, comprobamos que el campo de una bobina circular sobre su eje es máximo en el centro y disminuye de forma no lineal con la distancia, con la forma que predice la ley de Biot-Savart. Obtuvimos una permeabilidad magnética promedio de uno coma ciento sesenta por diez a la menos seis teslas metro por amperio, con un error del siete coma siete por ciento, reproducible y de origen sistemático. La componente perpendicular no fue nula porque el sensor quedó inclinado entre tres y cinco grados. Y vimos que dos bobinas separadas una distancia igual a su radio producen un campo mayor y casi uniforme en la región central, que es justo el objetivo del arreglo de Helmholtz.

---

## Lo que necesito que confirmes
1. ¿Apruebas el guion o qué cambias?
2. **Cuestionario:** el informe no trae preguntas de la guía resueltas (el Lab 4 sí tenía las figuras de bombillas). Si la guía de la Experiencia 6 tiene cuestionario, envíamelo en texto o foto y lo agrego como bloque.
3. **Video crudo:** súbelo a Drive como «Cualquier persona con el enlace» y pégame el link. Con él ajusto el bloque 4 y elijo los planos de fondo.
4. Formato 16:9 como el Lab 4, sin música y sin audio ambiente, salvo que me digas otra cosa.
