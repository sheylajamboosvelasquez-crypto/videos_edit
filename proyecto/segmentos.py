# Segmentos del video del Lab 4: lo que se narra (say), lo que se subtitula (sub)
# y lo que se ve (visual). Todo sale del informe lab4.docx y del guion v2 aprobado.
# - cue: fragmento del texto narrado; el elemento aparece cuando la voz llega ahí.
# - Rangos de video crudo en segundos: (inicio, fin, orientación "h" o "v").

MIEMBROS = ["Miguel Henríquez", "Iván Valdeblanquez", "David Jamboos", "Christian Charris", "Ian Tinoco"]

SEGMENTOS = [
    # ---------------- Bloque 0: portada ----------------
    dict(id="b0", visual=dict(kind="title", bg="img/grupo.jpg",
        title="Circuitos resistivos y ley de Ohm", kicker="Experiencia N.º 4 · Física de campos",
        members=MIEMBROS, footer="Grupo 26253 · Universidad de la Costa (CUC) · Docente: Lic. Diana Delgado González · 07/10/26"),
        say="En este video presentamos la experiencia número cuatro de Física de campos: circuitos resistivos y ley de Ohm. "
            "Veremos el montaje, la teoría, los cálculos y el cuestionario resuelto."),

    # ---------------- Bloque 1: objetivos ----------------
    dict(id="b1", visual=dict(kind="bullets", heading="Objetivos", bg="img/placa.jpg",
        lead=dict(text="Analizar experimentalmente la corriente, el voltaje y la resistencia equivalente en serie y en paralelo, verificando la ley de Ohm.", cue="El objetivo general"),
        items=[
            dict(text="Identificar resistencias: código de colores y óhmetro", cue="identificamos"),
            dict(text="Calcular y medir la resistencia equivalente", cue="calculamos"),
            dict(text="Comparar corrientes y voltajes en cada elemento", cue="comparamos"),
            dict(text="Explicar el brillo de bombillas en distintos arreglos", cue="explicamos"),
        ]),
        say="El objetivo general es analizar experimentalmente la corriente, el voltaje y la resistencia equivalente en circuitos en serie y en paralelo, "
            "verificando la ley de Ohm. Para lograrlo, identificamos las resistencias con el código de colores y el óhmetro, calculamos y medimos la resistencia equivalente, "
            "comparamos corrientes y voltajes en cada elemento y explicamos el brillo de bombillas en distintos arreglos."),

    # ---------------- Bloque 2: marco teórico ----------------
    dict(id="b2a", visual=dict(kind="equations", heading="Marco teórico · Ley de Ohm", eqs=[dict(src="eq/01.png", cue="La ley", big=True)],
        note=dict(text="Material óhmico (lineal): cumple la ley de Ohm", cue="Los materiales")),
        say="La ley de Ohm dice que la corriente en un conductor es directamente proporcional al voltaje entre sus extremos e inversamente proporcional a su resistencia. "
            "Los materiales que la cumplen se llaman óhmicos o lineales."),
    dict(id="b2b", visual=dict(kind="circuit", mode="serie", heading="Conexión en serie", eq="eq/02.png",
        facts=[dict(text="Misma corriente en todas: I₁ = I₂ = I₃", cue="La corriente"),
               dict(text="El voltaje se reparte: V = V₁ + V₂ + V₃", cue="el voltaje de la fuente"),
               dict(text="Req mayor que cualquiera de ellas", cue="y la resistencia equivalente")]),
        say="En serie, las resistencias van una tras otra. La corriente es la misma en todas, el voltaje de la fuente se reparte entre ellas, "
            "y la resistencia equivalente es la suma de todas, siempre mayor que cualquiera de ellas."),
    dict(id="b2c", visual=dict(kind="circuit", mode="paralelo", heading="Conexión en paralelo", eq="eq/03.png",
        facts=[dict(text="Mismo voltaje en cada rama: V = V₁ = V₂ = V₃", cue="El voltaje"),
               dict(text="La corriente se divide: I = I₁ + I₂ + I₃", cue="la corriente total"),
               dict(text="Req menor que la más pequeña", cue="y la equivalente")]),
        say="En paralelo, todas las resistencias se conectan a los mismos dos puntos. El voltaje es igual en cada rama, la corriente total se divide, "
            "pasando más corriente por la rama de menor resistencia, y la equivalente es menor que la más pequeña."),
    dict(id="b2d", visual=dict(kind="bullets", heading="Leyes de Kirchhoff y potencia",
        items=[dict(text="Lazo: la suma de las caídas de voltaje es igual al voltaje de la fuente", cue="en un lazo"),
               dict(text="Nodo: la corriente que entra es igual a la que sale", cue="en un nodo"),
               dict(text="En una bombilla, a mayor potencia, mayor brillo", cue="en una bombilla")],
        eq=dict(src="eq/04.png", cue="Además")),
        say="Estas reglas salen de las leyes de Kirchhoff: en un lazo, las caídas de voltaje suman el voltaje de la fuente, y en un nodo, la corriente que entra es igual a la que sale. "
            "Además, una resistencia disipa potencia en forma de calor; en una bombilla, a mayor potencia, mayor brillo."),
    dict(id="b2e", visual=dict(kind="measure", heading="Código de colores y uso del multímetro", eq="eq/05.png",
        cards=[dict(title="Resistencia", text="Óhmetro con el circuito desenergizado", cue="la resistencia se mide"),
               dict(title="Voltaje", text="Voltímetro en paralelo con el elemento", cue="el voltaje en paralelo"),
               dict(title="Corriente", text="Amperímetro en serie", cue="y la corriente")]),
        say="Las resistencias comerciales traen un código de colores con su valor nominal y su tolerancia; la banda dorada indica más o menos cinco por ciento. "
            "Con el multímetro, la resistencia se mide sin energía, el voltaje en paralelo con el elemento, y la corriente con el instrumento en serie."),

    # ---------------- Bloque 3: materiales ----------------
    dict(id="b3", visual=dict(kind="footage", clips=[
            dict(r=(49.6, 53.0, "h"), label="Multímetro digital Fluke 115", cue="Usamos"),
            dict(r=(154.0, 160.0, "h"), label="Laboratorio electrónico PASCO EM-8656", cue="el laboratorio"),
            dict(r=(205.5, 209.2, "v"), label="Interfaz PASCO 850", cue="la interfaz"),
            dict(r=(85.1, 86.4, "h"), label="Software PASCO Capstone", cue="el software"),
            dict(r=(166.0, 172.0, "h"), label="Resistencias, fuente de 10 V y cables", cue="tres resistencias")]),
        say="Usamos un multímetro Fluke ciento quince, el laboratorio electrónico EM ocho mil seiscientos cincuenta y seis de Pasco, la interfaz PASCO ochocientos cincuenta "
            "con el software Capstone y un sensor de voltaje, tres resistencias, una protoboard, una fuente de diez voltios y cables.",
        sub="Usamos un multímetro Fluke 115, el laboratorio electrónico EM-8656 de PASCO, la interfaz PASCO 850 con el software Capstone y un sensor de voltaje, "
            "tres resistencias, una protoboard, una fuente de 10 V y cables."),

    # ---------------- Bloque 4: montaje ----------------
    dict(id="b4a", visual=dict(kind="footage", clips=[
            dict(r=(211.5, 222.0, "v"), label="Medición de cada resistencia con el óhmetro", cue="Primero"),
            dict(r=(176.0, 190.0, "v"), label="Óhmetro: siempre sin energía", cue="Las medimos")]),
        say="Primero identificamos cada resistencia. R uno y R dos son de trescientos treinta ohmios y R tres de quinientos sesenta, "
            "todas con cinco por ciento de tolerancia. Las medimos con el óhmetro, siempre sin energía.",
        sub="Primero identificamos cada resistencia. R1 y R2 son de 330 Ω y R3 de 560 Ω, todas con 5 % de tolerancia. Las medimos con el óhmetro, siempre sin energía."),
    dict(id="b4b", visual=dict(kind="footage", clips=[
            dict(r=(392.0, 400.5, "v"), label="Circuito en serie: R1, R2 y R3 una tras otra", cue="Luego armamos"),
            dict(r=(164.0, 171.5, "h"), label="Cable rojo al mayor potencial, negro al menor", cue="con el cable rojo"),
            dict(r=(171.6, 173.8, "h"), label="Equivalente con la fuente desconectada", cue="Con la fuente"),
            dict(r=(122.0, 134.0, "v"), label="Medición en cada resistencia", cue="Después energizamos"),
            dict(r=(292.0, 296.0, "v"), label="Lectura del sensor en PASCO Capstone", cue="con el sensor"),
            dict(r=(264.0, 274.0, "v"), label="Multímetro como amperímetro, en serie", cue="y la corriente")]),
        say="Luego armamos el circuito en serie, con el cable rojo al mayor potencial y el negro al menor. Con la fuente desconectada medimos la resistencia equivalente. "
            "Después energizamos con diez voltios, medimos el voltaje en cada resistencia con el sensor de la interfaz, en paralelo, "
            "y la corriente del lazo con el multímetro como amperímetro, en serie.",
        sub="Luego armamos el circuito en serie, con el cable rojo al mayor potencial y el negro al menor. Con la fuente desconectada medimos la resistencia equivalente. "
            "Después energizamos con 10 V, medimos el voltaje en cada resistencia con el sensor de la interfaz, en paralelo, "
            "y la corriente del lazo con el multímetro como amperímetro, en serie."),
    dict(id="b4c", visual=dict(kind="footage", clips=[
            dict(r=(158.5, 161.8, "h"), label="Conexión de las resistencias en la placa", cue="Después conectamos"),
            dict(r=(225.0, 237.0, "v"), label="Equivalente sin energía", cue="Medimos la resistencia"),
            dict(r=(237.0, 252.0, "v"), label="Voltaje y corriente con la fuente encendida", cue="y con la fuente"),
            dict(r=(72.0, 76.0, "h"), label="Registro de los datos", cue="y la total")]),
        say="Después conectamos las tres resistencias entre los mismos dos nodos, en paralelo. Medimos la resistencia equivalente sin energía, "
            "y con la fuente encendida medimos el voltaje y la corriente de cada rama y la total."),

    # ---------------- Bloque 5: resultados ----------------
    dict(id="b5a", visual=dict(kind="table", heading="Tabla 1 · Reconocimiento y medida de resistencias",
        cols=["", "Nominal (Ω)", "Tol. (%)", "Tol. (Ω)", "Medido (Ω)"],
        rows=[["R1", "330", "5", "16,5", "328,2"], ["R2", "330", "5", "16,5", "328,0"], ["R3", "560", "5", "28,0", "554,4"]],
        marks=[dict(row=0, col=4, cue="trescientos veintiocho coma dos"), dict(row=1, col=4, cue="trescientos veintiocho coma cero"),
               dict(row=2, col=4, cue="quinientos cincuenta y cuatro")]),
        say="Las resistencias midieron trescientos veintiocho coma dos, trescientos veintiocho coma cero y quinientos cincuenta y cuatro coma cuatro ohmios, "
            "todas dentro de su tolerancia.",
        sub="Las resistencias midieron 328,2 Ω, 328,0 Ω y 554,4 Ω, todas dentro de su tolerancia."),
    dict(id="b5b", visual=dict(kind="table", heading="Tabla 2 · Asociación en serie",
        cols=["", "R medida (Ω)", "V teór. (V)", "V med. (V)", "I teór. (A)", "I med. (A)"],
        rows=[["R1", "328,2", "2,70", "2,66", "0,0082", "0,009"], ["R2", "328,0", "2,70", "2,70", "0,0082", "0,009"],
              ["R3", "554,4", "4,59", "4,56", "0,0082", "0,009"], ["Req / Total", "1210,6", "10,00", "9,92", "0,0082", "0,009"]],
        marks=[dict(col=5, cue="la corriente fue la misma"), dict(row=0, col=3, cue="dos coma sesenta y seis"),
               dict(row=1, col=3, cue="dos coma setenta en"), dict(row=2, col=3, cue="cuatro coma cincuenta y seis")]),
        say="En serie, la corriente fue la misma en todo el lazo, cero coma cero cero nueve amperios, y el voltaje se repartió: "
            "dos coma sesenta y seis voltios en R uno, dos coma setenta en R dos, y cuatro coma cincuenta y seis en R tres.",
        sub="En serie, la corriente fue la misma en todo el lazo, 0,009 A, y el voltaje se repartió: 2,66 V en R1, 2,70 V en R2 y 4,56 V en R3."),
    dict(id="b5c", visual=dict(kind="table", heading="Tabla 3 · Asociación en paralelo",
        cols=["", "R medida (Ω)", "V teór. (V)", "V med. (V)", "I teór. (A)", "I med. (A)"],
        rows=[["R1", "328,2", "10,00", "9,95", "0,0303", "0,031"], ["R2", "328,0", "10,00", "9,95", "0,0303", "0,031"],
              ["R3", "554,4", "10,00", "9,95", "0,0179", "0,017"], ["Req / Total", "126,8", "10,00", "9,95", "0,0785", "0,079"]],
        marks=[dict(col=3, cue="cada rama"), dict(row=0, col=5, cue="cero coma cero treinta y uno"), dict(row=2, col=5, cue="cero coma cero diecisiete")]),
        say="En paralelo, cada rama recibió nueve coma noventa y cinco voltios, y la corriente se dividió: cero coma cero treinta y uno amperios en R uno y R dos, "
            "y cero coma cero diecisiete amperios en R tres, la de mayor resistencia.",
        sub="En paralelo, cada rama recibió 9,95 V, y la corriente se dividió: 0,031 A en R1 y R2, y 0,017 A en R3, la de mayor resistencia."),

    # ---------------- Bloque 6: cálculos nominales ----------------
    dict(id="b6a", visual=dict(kind="equations", heading="Cálculos con valores nominales · Serie", eqs=[
            dict(src="eq/06.png", cue="Con los valores"), dict(src="eq/07.png", cue="La corriente"),
            dict(src="eq/08.png", cue="Así, R uno"), dict(src="eq/09.png", cue="y R tres"),
            dict(src="eq/10.png", cue="Sumados"), dict(src="eq/11.png", cue="La potencia")]),
        say="Con los valores nominales, la resistencia equivalente en serie es trescientos treinta, más trescientos treinta, más quinientos sesenta: mil doscientos veinte ohmios. "
            "La corriente es diez voltios entre mil doscientos veinte ohmios: cero coma cero cero ochenta y dos amperios. "
            "Así, R uno y R dos tienen dos coma setenta voltios cada una, y R tres cuatro coma cincuenta y nueve. "
            "Sumados dan diez voltios, el voltaje de la fuente. La potencia total es cero coma cero ochenta y dos vatios.",
        sub="Con los valores nominales, la resistencia equivalente en serie es 330 + 330 + 560 = 1220 Ω. La corriente es 10 V / 1220 Ω = 0,0082 A. "
            "Así, R1 y R2 tienen 2,70 V cada una, y R3 4,59 V. Sumados dan 10 V, el voltaje de la fuente. La potencia total es 0,082 W."),
    dict(id="b6b", visual=dict(kind="equations", heading="Cálculos con valores nominales · Paralelo", eqs=[
            dict(src="eq/12.png", cue="En paralelo"), dict(src="eq/13.png", cue="Su inverso"),
            dict(src="eq/14.png", cue="Cada rama"), dict(src="eq/15.png", cue="y la de quinientos"),
            dict(src="eq/16.png", cue="La corriente total"), dict(src="eq/17.png", cue="La corriente total"),
            dict(src="eq/18.png", cue="y la potencia")]),
        say="En paralelo, sumamos los inversos: uno entre trescientos treinta, dos veces, más uno entre quinientos sesenta, da cero coma cero cero siete ocho cuatro seis. "
            "Su inverso es ciento veintisiete coma cinco ohmios. Cada rama de trescientos treinta ohmios lleva cero coma cero trescientos tres amperios, "
            "y la de quinientos sesenta, cero coma cero ciento setenta y nueve. La corriente total es cero coma cero setecientos ochenta y cinco amperios, "
            "y la potencia, cero coma setecientos ochenta y cinco vatios.",
        sub="En paralelo, sumamos los inversos: 1/330 + 1/330 + 1/560 = 0,007846 Ω⁻¹. Su inverso es 127,5 Ω. Cada rama de 330 Ω lleva 0,0303 A, "
            "y la de 560 Ω, 0,0179 A. La corriente total es 0,0785 A, y la potencia, 0,785 W."),

    # ---------------- Bloque 7: cálculos medidos y errores ----------------
    dict(id="b7a", visual=dict(kind="equations", heading="Cálculos con valores medidos", eqs=[
            dict(src="eq/19.png", cue="Con los valores"), dict(src="eq/20.png", cue="y los voltajes"),
            dict(src="eq/24.png", cue="En paralelo"), dict(src="eq/22.png", cue="El óhmetro"), dict(src="eq/23.png", cue="El óhmetro")],
        note=dict(text="Óhmetro en paralelo: 126,8 Ω", cue="El óhmetro")),
        say="Con los valores medidos, la equivalente en serie es mil doscientos diez coma seis ohmios, y los voltajes suman nueve coma noventa y dos voltios, "
            "lo que confirma la ley de voltajes de Kirchhoff. En paralelo, las corrientes de rama suman cero coma cero setenta y nueve amperios, "
            "igual a la total medida, lo que confirma la ley de corrientes. El óhmetro marcó ciento veintiséis coma ocho ohmios.",
        sub="Con los valores medidos, la equivalente en serie es 1210,6 Ω, y los voltajes suman 9,92 V, lo que confirma la ley de voltajes de Kirchhoff. "
            "En paralelo, las corrientes de rama suman 0,079 A, igual a la total medida, lo que confirma la ley de corrientes. El óhmetro marcó 126,8 Ω."),
    dict(id="b7b", visual=dict(kind="equations", heading="Errores relativos", eqs=[
            dict(src="eq/26.png", cue="el error fue"), dict(src="eq/27.png", cue="y cero coma cincuenta y cinco"),
            dict(src="eq/21.png", cue="Por ley de Ohm"), dict(src="eq/28.png", cue="nueve coma sesenta y seis"),
            dict(src="eq/25.png", cue="En paralelo, el error"), dict(src="eq/29.png", cue="En paralelo, el error")]),
        say="Comparando con la teoría, el error fue de cero coma setenta y siete por ciento en serie y cero coma cincuenta y cinco por ciento en paralelo, dentro de la tolerancia. "
            "Por ley de Ohm, en serie el error subió a nueve coma sesenta y seis por ciento, porque la corriente medida, cero coma cero cero nueve amperios, "
            "es cerca de un diez por ciento mayor que la teórica; esto se atribuye a la lectura o a la escala del amperímetro. "
            "En paralelo, el error fue de uno coma veinticinco por ciento.",
        sub="Comparando con la teoría, el error fue de 0,77 % en serie y 0,55 % en paralelo, dentro de la tolerancia. "
            "Por ley de Ohm, en serie el error subió a 9,66 %, porque la corriente medida, 0,009 A, es cerca de un 10 % mayor que la teórica; "
            "esto se atribuye a la lectura o a la escala del amperímetro. En paralelo, el error fue de 1,25 %."),

    # ---------------- Bloque 8: cuestionario ----------------
    dict(id="b8a", visual=dict(kind="bulbs", fig="a", heading="Cuestionario · Figura a: dos bombillas en serie",
        facts=[dict(text="Cada bombilla recibe V/2", cue="cada una recibe"), dict(text="Potencia: (1/2)² = 1/4 → brillo tenue", cue="Con la mitad")]),
        say="Figura a: dos bombillas en serie. Comparten un solo camino, así que cada una recibe la mitad del voltaje. "
            "Con la mitad del voltaje, disipa la cuarta parte de la potencia, y por eso brillan de forma tenue."),
    dict(id="b8b", visual=dict(kind="bulbs", fig="b", heading="Cuestionario · Figura b: dos bombillas en paralelo",
        facts=[dict(text="Cada bombilla recibe el voltaje completo V", cue="Cada una recibe"), dict(text="Máximo brillo, igual en ambas", cue="así que brillan"),
               dict(text="Si una se desconecta, la otra sigue encendida", cue="Si una")]),
        say="Figura b: dos bombillas en paralelo. Cada una recibe el voltaje completo de la batería, de forma independiente, así que brillan con su máxima intensidad y por igual. "
            "Si una se desconecta, la otra sigue encendida."),
    dict(id="b8c", visual=dict(kind="bulbs", fig="c", heading="Cuestionario · Figura c: arreglo mixto",
        facts=[dict(text="Bloque L2 ∥ L3 = R/2", cue="Ese bloque"), dict(text="L1 recibe 2V/3 · L2 y L3 reciben V/3", cue="así que L uno"),
               dict(text="P(L1) = 4 × P(L2) = 4 × P(L3)", cue="y disipa")]),
        say="Figura c: L uno en serie con el bloque en paralelo de L dos y L tres. Ese bloque tiene la mitad de la resistencia de una bombilla, "
            "así que L uno se queda con dos tercios del voltaje y L dos y L tres con un tercio. Por eso L uno brilla más, y disipa cuatro veces la potencia de L dos o de L tres.",
        sub="Figura c: L1 en serie con el bloque en paralelo de L2 y L3. Ese bloque tiene la mitad de la resistencia de una bombilla, "
            "así que L1 se queda con dos tercios del voltaje y L2 y L3 con un tercio. Por eso L1 brilla más, y disipa cuatro veces la potencia de L2 o de L3."),

    # ---------------- Bloque 9: conclusiones ----------------
    dict(id="b9", visual=dict(kind="bullets", heading="Conclusiones", bg="img/placa2.jpg", items=[
            dict(text="Se validaron la ley de Ohm y las leyes de Kirchhoff", cue="se validaron"),
            dict(text="Req en serie (1210,6 Ω) ≈ 9,5 × Req en paralelo (126,8 Ω)", cue="La resistencia equivalente"),
            dict(text="Óhmetro vs. teoría: error < 1 % (0,77 % y 0,55 %)", cue="Las medidas"),
            dict(text="Con 10 V: 0,785 W en paralelo frente a 0,082 W en serie", cue="Y la forma")]),
        say="En conclusión, se validaron la ley de Ohm y las leyes de Kirchhoff. La resistencia equivalente en serie fue unas nueve coma cinco veces mayor que en paralelo. "
            "Las medidas con el óhmetro coincidieron con la teoría con errores menores al uno por ciento. "
            "Y la forma de conectar el circuito define el voltaje y la potencia de cada elemento: con los mismos diez voltios, el paralelo disipa casi diez veces más potencia que la serie.",
        sub="En conclusión, se validaron la ley de Ohm y las leyes de Kirchhoff. La resistencia equivalente en serie fue unas 9,5 veces mayor que en paralelo. "
            "Las medidas con el óhmetro coincidieron con la teoría con errores menores al 1 %. "
            "Y la forma de conectar el circuito define el voltaje y la potencia de cada elemento: con los mismos 10 V, el paralelo disipa casi diez veces más potencia que la serie."),
    dict(id="b10", silent=4.0, visual=dict(kind="title", bg="img/grupo.jpg", title="Gracias", kicker="Experiencia N.º 4 · Circuitos resistivos y ley de Ohm",
        members=MIEMBROS, footer="Física de campos · Grupo 26253 · Universidad de la Costa (CUC)"), say=""),
]

# ---------------- v2: video del grupo de fondo ----------------
# Planos útiles del crudo, en orden (inicio, fin, orientación). Se excluyen planos
# borrosos, de bata o piso, y los momentos con la persona que parece la docente
# (≈3:16-3:26, 4:49-4:52, 5:45-5:50).
FONDO = [
    (0.0, 3.8, "v"), (4.2, 7.8, "h"), (8.2, 34.0, "v"), (36.5, 48.4, "v"),
    (49.2, 69.0, "h"), (71.0, 79.0, "h"), (81.5, 86.4, "h"),
    (86.6, 99.0, "v"), (103.0, 111.5, "v"), (113.5, 136.5, "v"), (138.5, 146.4, "v"),
    (147.1, 173.8, "h"),
    (174.1, 196.0, "v"), (206.0, 241.0, "v"), (243.5, 256.5, "v"), (264.0, 276.5, "v"),
    (279.0, 281.5, "v"), (283.5, 289.0, "v"), (292.0, 299.0, "v"), (311.5, 321.5, "v"),
    (324.0, 331.5, "v"), (334.0, 345.0, "v"), (350.0, 358.0, "v"), (362.0, 369.0, "v"),
    (371.5, 386.0, "v"), (389.0, 400.5, "v"),
]
FONDO_FIJO = {"b10": [(0.0, 3.8, "v")]}  # cierre: la foto del grupo
