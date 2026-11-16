# Experiencia 6: Bobina de Helmholtz. Tramos del video (guion v1 aprobado en lo esencial).
# Datos: solo los del informe. Rangos de clips: ("cN", inicio, fin) dentro del clip N (ver offsets.json).

NOMBRE = "lab6_helmholtz"
CRUDO = "salida/lab6/trabajo/crudo_lab6_1080.mp4"  # los 10 clips de WhatsApp unidos y compuestos a 1080p
MIEMBROS = ["Miguel Henríquez", "Iván Valdeblanquez", "David Jamboos", "Christian Charris", "Ian Tinoco"]
PIE = "Física de campos · Grupo 26253 · Universidad de la Costa (CUC)"

SEGMENTOS = [
    # ---------------- 0. Portada (pantalla completa, foto del grupo) ----------------
    dict(id="b0", fondo=False, visual=dict(kind="title", bg="img6/grupo.jpg", theme="mag",
        title="Bobina de Helmholtz", kicker="Experiencia N.º 6 · Campo magnético de una bobina circular",
        members=MIEMBROS, footer=PIE + " · Docente: Lic. Diana Delgado González · 15/11/26"),
        say="En este video presentamos la experiencia número seis de Física de campos: la bobina de Helmholtz y el campo magnético de una bobina circular. "
            "Veremos el montaje, la teoría, los resultados, los cálculos y las conclusiones."),

    # ---------------- 1. Objetivos ----------------
    dict(id="b1", visual=dict(kind="bullets", heading="Objetivos",
        lead=dict(text="Analizar la distribución espacial de la intensidad del campo magnético generado por una bobina de Helmholtz.", cue="El objetivo general"),
        items=[dict(text="Medir las componentes axial y perpendicular del campo sobre el eje", cue="medimos"),
               dict(text="Comparar la curva experimental con el ajuste y con el modelo teórico", cue="comparamos la curva"),
               dict(text="Calcular μ₀ experimental y su porcentaje de error", cue="calculamos"),
               dict(text="Comparar una bobina con el par de Helmholtz", cue="comparamos el perfil")]),
        say="El objetivo general es analizar cómo se distribuye en el espacio la intensidad del campo magnético que genera una bobina de Helmholtz. "
            "Para lograrlo, medimos las componentes axial y perpendicular del campo a lo largo del eje de una bobina circular, "
            "comparamos la curva experimental con el ajuste del programa y con el modelo teórico, "
            "calculamos el valor experimental de la permeabilidad del vacío con su porcentaje de error, "
            "y comparamos el perfil de una sola bobina con el que se espera para el par de Helmholtz."),

    # ---------------- 2. Marco teórico ----------------
    dict(id="b2a", visual=dict(kind="coil", heading="Marco teórico · Campo en el eje de una bobina", eq="eq6/eq1.png",
        facts=[dict(text="Cada elemento de corriente aporta un dB ∝ 1/r²", cue="cada pedacito"),
               dict(text="Sobre el eje, las componentes perpendiculares se cancelan por pares", cue="las componentes perpendiculares"),
               dict(text="Queda solo la componente axial", cue="solo queda")],
        eqcue="Para una bobina"),
        say="El campo magnético lo producen las cargas en movimiento, y su unidad es el tesla. La ley de Biot Savart dice que cada pedacito de corriente aporta un campo "
            "que disminuye con el cuadrado de la distancia. Sobre el eje de una bobina circular el cálculo se simplifica: las componentes perpendiculares se cancelan por pares "
            "y solo queda la componente axial. Para una bobina de ene espiras y radio erre, el campo a una distancia equis del centro es mu cero por ene por i por erre al cuadrado, "
            "dividido entre dos veces, equis al cuadrado más erre al cuadrado, elevado a tres medios.",
        sub="El campo magnético lo producen las cargas en movimiento, y su unidad es el tesla. La ley de Biot-Savart dice que cada pedacito de corriente aporta un campo "
            "que disminuye con el cuadrado de la distancia. Sobre el eje de una bobina circular el cálculo se simplifica: las componentes perpendiculares se cancelan por pares "
            "y solo queda la componente axial. Para una bobina de N espiras y radio R, el campo a una distancia x del centro es B = μ₀·N·I·R² / [2(x² + R²)^(3/2)]."),
    dict(id="b2b", visual=dict(kind="equations", heading="Campo en el centro y permeabilidad del vacío",
        eqs=[dict(src="eq6/eq2.png", cue="En el centro"), dict(src="eq6/eq3.png", cue="Y de ahí")],
        note=dict(text="μ₀ = 4π × 10⁻⁷ ≈ 1,257 × 10⁻⁶ T·m/A", cue="Su valor de referencia"),
        counter=dict(label="Lejos de la bobina", text="B ∝ 1/x³ (como un dipolo)", cue="decae")),
        say="El campo es máximo en el centro de la bobina, y lejos de ella decae como uno sobre equis al cubo, igual que un dipolo magnético. "
            "En el centro, la ecuación se reduce a mu cero por ene por i, entre dos erre. Y de ahí despejamos la permeabilidad magnética del vacío: "
            "mu cero es igual a dos erre por el campo en el centro, dividido entre ene por i. "
            "Su valor de referencia es uno coma doscientos cincuenta y siete por diez a la menos seis teslas metro por amperio.",
        sub="El campo es máximo en el centro de la bobina, y lejos de ella decae como 1/x³, igual que un dipolo magnético. "
            "En el centro, la ecuación se reduce a B(0) = μ₀·N·I / (2R). Y de ahí despejamos la permeabilidad magnética del vacío: "
            "μ₀ = 2R·B(0) / (N·I). Su valor de referencia es 1,257 × 10⁻⁶ T·m/A."),
    dict(id="b2c", visual=dict(kind="helmholtz", heading="Sensor inclinado, par de Helmholtz y error",
        eqs=[dict(src="eq6/eq4.png", cue="Si el sensor"), dict(src="eq6/eq5.png", cue="producen en el punto medio"), dict(src="eq6/eq6.png", cue="Y para comparar")],
        pairCue="En el arreglo de Helmholtz"),
        say="Por simetría, la componente perpendicular del campo debería ser cero sobre el eje. Si el sensor queda inclinado un ángulo theta, "
            "registra una parte del campo axial en el canal perpendicular, y ese ángulo se estima con el arcotangente del cociente entre las dos componentes. "
            "En el arreglo de Helmholtz, dos bobinas iguales separadas una distancia igual a su radio producen en el punto medio un campo casi uniforme, "
            "que vale cuatro quintos elevado a tres medios, por mu cero por ene por i, sobre erre. Y para comparar con la referencia usamos el error relativo porcentual.",
        sub="Por simetría, la componente perpendicular del campo debería ser cero sobre el eje. Si el sensor queda inclinado un ángulo θ, "
            "registra una parte del campo axial en el canal perpendicular, y ese ángulo se estima con θ ≈ arctan(B⊥/Bax). "
            "En el arreglo de Helmholtz, dos bobinas iguales separadas una distancia igual a su radio producen en el punto medio un campo casi uniforme, "
            "B_H = (4/5)^(3/2) · μ₀·N·I / R. Y para comparar con la referencia usamos el error relativo porcentual."),

    # ---------------- 3. Materiales (pantalla completa, clips) ----------------
    dict(id="b3", visual=dict(kind="footage", clips=[
            dict(r=("c8", 0.0, 4.0), label="Bobina circular · N = 500 espiras · R = 10,06 cm", cue="Usamos"),
            dict(r=("c7", 4.0, 8.4), label="Sensor de campo magnético de dos ejes", cue="un sensor"),
            dict(r=("c6", 11.6, 15.5), label="Interfaz universal PASCO 850", cue="la interfaz"),
            dict(r=("c7", 21.0, 25.4), label="Software PASCO Capstone", cue="Capstone"),
            dict(r=("c7", 0.0, 4.0), label="Pista y soportes para desplazar el sensor", cue="y una pista")]),
        say="Usamos una bobina circular de quinientas espiras y diez coma cero seis centímetros de radio, un sensor de campo magnético de dos ejes, axial y perpendicular, "
            "la interfaz PASCO ochocientos cincuenta con el software Capstone, y una pista con soportes para desplazar el sensor a lo largo del eje de la bobina.",
        sub="Usamos una bobina circular de 500 espiras y 10,06 cm de radio, un sensor de campo magnético de dos ejes, axial y perpendicular, "
            "la interfaz PASCO 850 con el software Capstone, y una pista con soportes para desplazar el sensor a lo largo del eje de la bobina."),

    # ---------------- 4. Montaje y procedimiento (clips) ----------------
    dict(id="b4a", visual=dict(kind="footage", clips=[
            dict(r=("c10", 20.0, 24.5), label="Conexión de la bobina, el sensor y la interfaz", cue="Primero"),
            dict(r=("c8", 4.0, 8.5), label="Sonda en el centro de la bobina", cue="Deslizamos"),
            dict(r=("c4", 51.0, 57.0), label="Botón TARE: sensor en cero", cue="y presionamos")]),
        say="Primero conectamos la bobina, el sensor de campo y la interfaz según el montaje de la guía. Deslizamos el sensor por la pista hasta que la sonda quedó "
            "en el centro de la bobina, y presionamos el botón tare para poner el sensor en cero.",
        sub="Primero conectamos la bobina, el sensor de campo y la interfaz según el montaje de la guía. Deslizamos el sensor por la pista hasta que la sonda quedó "
            "en el centro de la bobina, y presionamos el botón TARE para poner el sensor en cero."),
    dict(id="b4b", visual=dict(kind="footage", clips=[
            dict(r=("c6", 7.7, 11.6), label="Generador de señales: 6,2 V de CC", cue="En el generador"),
            dict(r=("c2", 0.0, 4.0), label="Corriente de salida: 0,339–0,341 A", cue="la interfaz registró"),
            dict(r=("c8", 12.7, 16.9), label="Vista previa y Mantener muestra · 10 Hz", cue="Pulsamos")]),
        say="En el generador de señales de Capstone verificamos que el voltaje de corriente continua estuviera en seis coma dos voltios y lo encendimos; "
            "la interfaz registró una corriente de cero coma trescientos cuarenta y un amperios. Pulsamos vista previa, esperamos a que la medida se estabilizara "
            "y pulsamos mantener muestra, registrando las dos componentes del campo a diez hercios.",
        sub="En el generador de señales de Capstone verificamos que el voltaje de CC estuviera en 6,2 V y lo encendimos; "
            "la interfaz registró una corriente de 0,341 A. Pulsamos Vista previa, esperamos a que la medida se estabilizara "
            "y pulsamos Mantener muestra, registrando las dos componentes del campo a 10 Hz."),
    dict(id="b4c", visual=dict(kind="footage", clips=[
            dict(r=("c9", 16.0, 20.5), label="Barrido: de 3 en 3 cm, de 0 a 24 cm", cue="Repetimos"),
            dict(r=("c3", 12.0, 17.0), label="Nueve datos registrados", cue="para un total"),
            dict(r=("c7", 21.0, 25.4), label="Ajuste de curva definido por el usuario", cue="A los datos")]),
        say="Repetimos la medición desplazando el sensor de tres en tres centímetros, desde cero hasta veinticuatro centímetros, para un total de nueve datos. "
            "A los datos del campo axial les aplicamos un ajuste de curva definido por el usuario, con la forma de la ecuación uno.",
        sub="Repetimos la medición desplazando el sensor de 3 en 3 cm, desde 0 hasta 24 cm, para un total de nueve datos. "
            "A los datos del campo axial les aplicamos un ajuste de curva definido por el usuario, con la forma de la ecuación (1)."),
    dict(id="b4d", visual=dict(kind="footage", clips=[
            dict(r=("c4", 45.0, 51.0), label="Sensor en el centro, tres corrientes", cue="Por último"),
            dict(r=("c4", 34.0, 40.0), label="I = 0,383 A · B = 0,001086 T", cue="cero coma trescientos ochenta y tres"),
            dict(r=("c10", 28.0, 34.0), label="Lecturas para calcular μ₀", cue="para calcular")]),
        say="Por último, con el sensor en el centro, registramos el campo para tres corrientes: cero coma trescientos veintinueve, cero coma trescientos cincuenta y seis "
            "y cero coma trescientos ochenta y tres amperios, para calcular mu cero y su error.",
        sub="Por último, con el sensor en el centro, registramos el campo para tres corrientes: 0,329 A, 0,356 A y 0,383 A, para calcular μ₀ y su error."),

    # ---------------- 5. Resultados: perfil del campo ----------------
    dict(id="b5a", visual=dict(kind="table", heading="Tabla 1 · Campo axial y perpendicular (I = 0,341 A)",
        cols=["x (m)", "Bax (×10⁻⁴ T)", "B⊥ (×10⁻⁴ T)", "Bteór (×10⁻⁴ T)"],
        rows=[["0,00", "9,86", "0,917", "10,65"], ["0,03", "8,36", "0,643", "9,37"], ["0,06", "5,77", "0,332", "6,75"], ["0,09", "4,31", "0,191", "4,41"],
              ["0,12", "2,82", "0,127", "2,82"], ["0,15", "1,59", "0,0389", "1,84"], ["0,18", "0,443", "−0,133", "1,24"], ["0,21", "0,0569", "−0,243", "0,86"], ["0,24", "0,0561", "−0,225", "0,62"]],
        marks=[dict(row=0, col=1, cue="máximo en el centro"), dict(row=1, col=1, cue="a tres centímetros"), dict(row=5, col=1, cue="a quince"),
               dict(row=7, col=1, cue="a veintiún"), dict(row=8, col=1, cue="a veintiún")]),
        say="El campo axial fue máximo en el centro, cerca de nueve coma ochenta y seis por diez a la menos cuatro teslas, y fue cayendo con la distancia: "
            "a tres centímetros conservaba cerca del ochenta y cinco por ciento de su valor, a quince centímetros solo el dieciséis por ciento, "
            "y a veintiún y veinticuatro centímetros quedó en valores del orden de diez a la menos seis teslas.",
        sub="El campo axial fue máximo en el centro, cerca de 9,86 × 10⁻⁴ T, y fue cayendo con la distancia: "
            "a 3 cm conservaba cerca del 85 % de su valor, a 15 cm solo el 16 %, y a 21 y 24 cm quedó en valores del orden de 10⁻⁶ T."),
    dict(id="b5b", visual=dict(kind="figure", heading="Figura 1 · Ajuste definido por el usuario (Capstone)", src="fig6/fig1.png", reveal=True,
        facts=[dict(text="Forma de campana: máximo en el centro", cue="La curva"),
               dict(text="RMSE = 4,09 × 10⁻⁵ T", cue="error cuadrático"),
               dict(text="R ajustado 9,57 cm vs. 10,06 cm medido", cue="dio un radio"),
               dict(text="m, N e I no se interpretan por separado; solo su producto", cue="Los parámetros")]),
        say="La curva tiene la forma de campana que predice la ecuación uno. El ajuste definido por el usuario siguió esa tendencia con un error cuadrático medio "
            "de cuatro coma cero nueve por diez a la menos cinco teslas, y dio un radio de nueve coma cincuenta y siete centímetros, frente a los diez coma cero seis medidos. "
            "Los parámetros eme, ene e i del ajuste no se pueden interpretar por separado, porque el programa los reparte como quiere; solo tiene sentido su producto.",
        sub="La curva tiene la forma de campana que predice la ecuación (1). El ajuste definido por el usuario siguió esa tendencia con un RMSE "
            "de 4,09 × 10⁻⁵ T, y dio un radio de 9,57 cm, frente a los 10,06 cm medidos. "
            "Los parámetros m, N e I del ajuste no se pueden interpretar por separado, porque el programa los reparte como quiere; solo tiene sentido su producto."),
    dict(id="b5c", visual=dict(kind="figure", heading="Figura 3 · Experimental, ajuste y curva teórica", src="fig6/fig3.png", reveal=True,
        facts=[dict(text="Los datos quedan por debajo de la teoría en casi todo el recorrido", cue="los datos quedan"),
               dict(text="En el centro: 7,4 % menos que el valor teórico", cue="siete coma cuatro")]),
        say="Frente a la curva teórica, los datos quedan por debajo en casi todo el recorrido, y en el centro el campo medido es siete coma cuatro por ciento menor que el teórico.",
        sub="Frente a la curva teórica, los datos quedan por debajo en casi todo el recorrido, y en el centro el campo medido es 7,4 % menor que el teórico."),

    # ---------------- 6. Componente perpendicular ----------------
    dict(id="b6", visual=dict(kind="figure", heading="Figura 2 · Componente perpendicular", src="fig6/fig2.png", reveal=True, eq="eq6/eq4.png",
        facts=[dict(text="En el centro: B⊥ = 9,17 × 10⁻⁵ T (debería ser 0)", cue="registró"),
               dict(text="θ ≈ arctan(0,093) ≈ 5°: sensor inclinado", cue="arcotangente"),
               dict(text="Desde 18 cm se vuelve negativa: campo terrestre y deriva del cero", cue="Desde dieciocho")]),
        say="La componente perpendicular debería ser cero sobre el eje, pero en el centro el sensor registró nueve coma diecisiete por diez a la menos cinco teslas, "
            "y esa lectura bajó junto con el campo axial. Eso indica que el sensor estaba inclinado respecto al eje: con el arcotangente de cero coma cero noventa y tres, "
            "el ángulo es de unos cinco grados. Desde dieciocho centímetros la componente se volvió negativa, por el campo terrestre, que el tare solo compensa "
            "en el punto donde se presionó, y por la deriva del cero del sensor.",
        sub="La componente perpendicular debería ser cero sobre el eje, pero en el centro el sensor registró 9,17 × 10⁻⁵ T, "
            "y esa lectura bajó junto con el campo axial. Eso indica que el sensor estaba inclinado respecto al eje: con arctan(0,093), "
            "el ángulo es de unos 5°. Desde 18 cm la componente se volvió negativa, por el campo terrestre, que el TARE solo compensa "
            "en el punto donde se presionó, y por la deriva del cero del sensor."),

    # ---------------- 7. Cálculo de μ₀ y error ----------------
    dict(id="b7a", visual=dict(kind="table", heading="Tabla 3 · Permeabilidad con el campo en el centro",
        cols=["I (A)", "B(0) med. (T)", "B(0) teór. (T)", "μ₀,exp (T·m/A)"],
        rows=[["0,329", "9,490 × 10⁻⁴", "1,027 × 10⁻³", "1,1607 × 10⁻⁶"], ["0,356", "1,030 × 10⁻³", "1,112 × 10⁻³", "1,1642 × 10⁻⁶"], ["0,383", "1,100 × 10⁻³", "1,196 × 10⁻³", "1,1557 × 10⁻⁶"]],
        marks=[dict(row=0, col=0, cue="Para la primera"), dict(row=0, col=1, cue="campo de nueve"), dict(row=0, col=3, cue="mu cero da")],
        eqs=[dict(src="eq6/eq7.png", cue="mu cero da")]),
        say="Con el campo en el centro para cada corriente calculamos la permeabilidad. Para la primera, con radio de cero coma mil seis metros, "
            "campo de nueve coma cuarenta y nueve por diez a la menos cuatro teslas, quinientas espiras y cero coma trescientos veintinueve amperios, "
            "mu cero da uno coma mil seiscientos siete por diez a la menos seis teslas metro por amperio.",
        sub="Con el campo en el centro para cada corriente calculamos la permeabilidad. Para la primera, con R = 0,1006 m, "
            "B(0) = 9,49 × 10⁻⁴ T, N = 500 e I = 0,329 A, μ₀ = 1,1607 × 10⁻⁶ T·m/A."),
    dict(id="b7b", visual=dict(kind="table", heading="Tabla 4 · Error porcentual de μ₀",
        cols=["μ₀,exp (T·m/A)", "μ₀,teo (T·m/A)", "%E"],
        rows=[["1,1607 × 10⁻⁶", "1,257 × 10⁻⁶", "7,66"], ["1,1642 × 10⁻⁶", "1,257 × 10⁻⁶", "7,38"], ["1,1557 × 10⁻⁶", "1,257 × 10⁻⁶", "8,06"]],
        marks=[dict(row=0, col=2, cue="siete coma sesenta y seis"), dict(row=1, col=2, cue="siete coma treinta y ocho"), dict(row=2, col=2, cue="ocho coma cero seis")],
        eqs=[dict(src="eq6/eq8.png", cue="Su error")],
        counter=dict(label="μ₀ promedio", value="1,160 × 10⁻⁶ T·m/A", cue="el promedio")),
        say="Su error frente al valor de referencia es de siete coma sesenta y seis por ciento. Para las otras dos corrientes los errores fueron de "
            "siete coma treinta y ocho y ocho coma cero seis por ciento, y el promedio de mu cero fue uno coma ciento sesenta por diez a la menos seis.",
        sub="Su error frente al valor de referencia es de 7,66 %. Para las otras dos corrientes los errores fueron de 7,38 % y 8,06 %, "
            "y el promedio de μ₀ fue 1,160 × 10⁻⁶ T·m/A."),
    dict(id="b7c", visual=dict(kind="figure", heading="Figura 4 · Campo en el centro vs. corriente", src="fig6/fig4.png", reveal=True,
        facts=[dict(text="B(0) crece en proporción a I", cue="creció en proporción"),
               dict(text="Pendiente medida 2,883 mT/A · teórica 3,123 mT/A", cue="pendiente"),
               dict(text="De la pendiente: μ₀ = 1,160 × 10⁻⁶ T·m/A (7,7 % de error)", cue="sale el mismo")]),
        say="Además, el campo en el centro creció en proporción a la corriente: la recta de ajuste por el origen tiene una pendiente de dos coma ochocientos ochenta y tres "
            "militeslas por amperio, frente a tres coma ciento veintitrés de la recta teórica, y de esa pendiente sale el mismo mu cero, con siete coma siete por ciento de error.",
        sub="Además, el campo en el centro creció en proporción a la corriente: la recta de ajuste por el origen tiene una pendiente de 2,883 mT/A, "
            "frente a 3,123 mT/A de la recta teórica, y de esa pendiente sale el mismo μ₀, con 7,7 % de error."),

    # ---------------- 8. Análisis y par de Helmholtz ----------------
    dict(id="b8a", visual=dict(kind="bullets", heading="¿Por qué el error es sistemático?",
        lead=dict(text="Los tres errores difieren entre sí menos de un punto porcentual: algo redujo el campo de la misma forma en todas las pruebas.", cue="Los tres errores"),
        items=[dict(text="Posición de la sonda: 2 cm fuera del centro reducen el campo 5,7 %", cue="posición de la sonda"),
               dict(text="Radio efectivo del devanado (500 espiras con espesor)", cue="radio efectivo"),
               dict(text="Inclinación del sensor (≈ 5°)", cue="la inclinación"),
               dict(text="Calibración del sensor y del medidor de corriente", cue="la calibración")]),
        say="Los tres errores difieren entre sí menos de un punto porcentual, así que la causa es sistemática: algo redujo el campo medido de la misma forma en todas las pruebas. "
            "La más probable es la posición de la sonda, porque un desplazamiento de dos centímetros respecto al centro reduce el campo en cinco coma siete por ciento. "
            "También influyen el radio efectivo del devanado, la inclinación del sensor y la calibración del sensor y del medidor de corriente.",
        sub="Los tres errores difieren entre sí menos de un punto porcentual, así que la causa es sistemática: algo redujo el campo medido de la misma forma en todas las pruebas. "
            "La más probable es la posición de la sonda, porque un desplazamiento de 2 cm respecto al centro reduce el campo en 5,7 %. "
            "También influyen el radio efectivo del devanado, la inclinación del sensor y la calibración del sensor y del medidor de corriente."),
    dict(id="b8b", visual=dict(kind="figure", heading="Figura 5 · Una bobina frente al par de Helmholtz", src="fig6/fig5.png", reveal=True,
        facts=[dict(text="Una bobina: pico en el centro; a 5 cm pierde ≈ 28 %", cue="Una sola bobina"),
               dict(text="Par de Helmholtz: 1,43 × mayor en el centro (≈ 1,52 mT)", cue="uno coma cuarenta y tres"),
               dict(text="Meseta: varía < 0,5 % en ±2,5 cm", cue="forma una meseta"),
               dict(text="Por eso se usa para campos de referencia", cue="Por esa región")]),
        say="Por último, comparamos el perfil de una bobina con el par de Helmholtz. Una sola bobina produce un pico en el centro, y a cinco centímetros ya perdió "
            "cerca del veintiocho por ciento. Con dos bobinas separadas una distancia igual al radio, el campo en el punto medio es uno coma cuarenta y tres veces mayor, "
            "unos uno coma cincuenta y dos militeslas, y forma una meseta que varía menos del cero coma cinco por ciento en más menos dos coma cinco centímetros. "
            "Por esa región casi uniforme, el arreglo se usa para generar campos de referencia.",
        sub="Por último, comparamos el perfil de una bobina con el par de Helmholtz. Una sola bobina produce un pico en el centro, y a 5 cm ya perdió "
            "cerca del 28 %. Con dos bobinas separadas una distancia igual al radio, el campo en el punto medio es 1,43 veces mayor, "
            "unos 1,52 mT, y forma una meseta que varía menos del 0,5 % en ±2,5 cm. Por esa región casi uniforme, el arreglo se usa para generar campos de referencia."),

    # ---------------- 9. Conclusiones y cierre ----------------
    dict(id="b9", visual=dict(kind="bullets", heading="Conclusiones", items=[
            dict(text="El campo en el eje es máximo en el centro y cae de forma no lineal, como predice Biot-Savart", cue="comprobamos"),
            dict(text="μ₀ = 1,160 × 10⁻⁶ T·m/A, error 7,7 %, reproducible y sistemático", cue="Obtuvimos"),
            dict(text="B⊥ ≠ 0 por una inclinación del sensor de 3° a 5°", cue="La componente perpendicular"),
            dict(text="El par de Helmholtz da un campo mayor y casi uniforme en el centro", cue="Y vimos")]),
        say="En conclusión, comprobamos que el campo de una bobina circular sobre su eje es máximo en el centro y disminuye de forma no lineal con la distancia, "
            "con la forma que predice la ley de Biot Savart. Obtuvimos una permeabilidad magnética promedio de uno coma ciento sesenta por diez a la menos seis "
            "teslas metro por amperio, con un error del siete coma siete por ciento, reproducible y de origen sistemático. La componente perpendicular no fue nula "
            "porque el sensor quedó inclinado entre tres y cinco grados. Y vimos que dos bobinas separadas una distancia igual a su radio producen un campo mayor "
            "y casi uniforme en la región central, que es justo el objetivo del arreglo de Helmholtz.",
        sub="En conclusión, comprobamos que el campo de una bobina circular sobre su eje es máximo en el centro y disminuye de forma no lineal con la distancia, "
            "con la forma que predice la ley de Biot-Savart. Obtuvimos una permeabilidad magnética promedio de 1,160 × 10⁻⁶ T·m/A, con un error del 7,7 %, "
            "reproducible y de origen sistemático. La componente perpendicular no fue nula porque el sensor quedó inclinado entre 3° y 5°. "
            "Y vimos que dos bobinas separadas una distancia igual a su radio producen un campo mayor y casi uniforme en la región central, "
            "que es justo el objetivo del arreglo de Helmholtz."),
    dict(id="b10", fondo=False, silent=4.5, visual=dict(kind="title", bg="img6/grupo2.jpg", theme="mag", title="Gracias",
        kicker="Experiencia N.º 6 · Bobina de Helmholtz", members=MIEMBROS, footer=PIE), say=""),
]

# Rollo de fondo (grupo y equipo), en orden. Se excluyen cabezas tapando la cámara, cables sueltos y planos movidos.
FONDO = [
    ("c1", 8.5, 17.0), ("c2", 0.0, 16.5), ("c3", 0.0, 28.5), ("c4", 0.0, 11.0), ("c4", 17.0, 40.0), ("c4", 45.0, 57.0),
    ("c5", 0.0, 6.5), ("c6", 3.5, 15.5), ("c7", 0.0, 12.5), ("c7", 17.0, 25.0), ("c8", 0.0, 16.9),
    ("c9", 0.0, 8.0), ("c9", 12.0, 24.5), ("c10", 0.0, 16.0), ("c10", 20.0, 36.0),
]
FONDO_FIJO = {}
