import streamlit as st

# Interfaz con Streamlit
st.title("Simulación de Salario Docente - Decreto 1279")


#variables
valor_punto = 20895
# 📌 Variables de títulos universitarios
tipoTitulo = None
clinicas = 0
noClinicas = 0
maestrias = 0
doctorados = 0

# 📌 Variables de escalafón docente
escalafon = None

# 📌 Variables de experiencia calificada
eInves = 0
eDoc = 0
eCar = 0
eNoDoc = 0

# 📌 Variables de productividad académica
articulos_A1, articulos_A2, articulos_B, articulos_C = [], [], [], []
articulos_CA1, articulos_CA2, articulos_CB, articulos_CC = [], [], [], []
articulos_OA1, articulos_OA2, articulos_OB, articulos_OC= [], [], [], []
dImpInts, dImpNacs, librosInvs, librosTexs = [], [], [], []
librosEns, librosNacs, patentes, traLibs = [], [], [], []
imTrIns, imTrNas, inTecs, adTecs, prSos = [], [], [], [], []

# 📌 Definir los inputs de productividad académica si no se ingresan datos
artA1 = 0
artA2 = 0
artB = 0
artC = 0
artCA1 = 0
artCA2 = 0
artCB = 0
artCC = 0

# 📌 Puntos base según el Decreto 1279
puntajes_base = {
    "videos_int": 12, "videos_nac": 7,
    "libros_inv": 20, "libros_texto": 15, "libros_ensayo": 15,
    "premios": 15, "patentes": 25, "traducciones": 15,
    "obras_int": 20, "obras_nac": 14,
    "innovacion": 15, "adaptacion": 8, "software": 15,
    "A1": 15, "A2": 12, "B": 8, "C": 3
}

# Entrada de datos
st.subheader("1. TITULOS DE ESTUDIOS UNIVERSITARIOS")
st.write("- Por títulos de pregrado: Sólo si se ha obtenido el diploma. (Numeral 1, Artículo 7 Dc. 1279)")

tipoTitulo = st.radio("Area: ", ["En Medicina Humana o composición Musical", "En otra área"], index=None)

st.write("- Por títulos de Posgrado. (Numeral 2, Artículo 7 Dc. 1279)")
st.write("*Especializaciones (incluye subespecializaciones clínicas o médicas)*")

clinicas = st.number_input(">> Clínicas en Medicina Humana y Odontología:", min_value=0, step=1, key="clinicas", disabled=(tipoTitulo == "En otra área"))
noClinicas = st.number_input(">> No Clínicas:", min_value=0, step=1, key="noClinicas", disabled=(tipoTitulo == "En Medicina Humana o composición Musical"))
maestrias = st.number_input("Magister o Maestrías:", min_value=0, step=1, key="maestrias")
doctorados = st.number_input("Ph.D. o Doctorado:", min_value=0, step=1, key="doctorados")

st.subheader("2. CATEGORIAS DENTRO DEL ESCALAFON DOCENTE")
escalafon = st.radio("CATEGORIA:", ["Auxiliar", "Asistente", "Asociado", "Titular"])

st.subheader("3. EXPERIENCIA CALIFICADA")
eInves = st.number_input("- Experiencia Investigativa:", min_value=0, step=1)
eDoc = st.number_input("- Experiencia Docente:", min_value=0, step=1)
eCar = st.number_input("- Experiencia Cargos Dirección Académica:", min_value=0, step=1)
eNoDoc = st.number_input("- Experiencia no Docente:", min_value=0, step=1)

st.subheader("4. PRODUCTIVIDAD ACADEMICA")
st.write("Articulos:")
artA1 = st.number_input("Artículos en revistas indexadas por MINCIENCIAS A1", min_value=0, max_value=30, step=1, key="a1")
if artA1 > 0:
    with st.expander("📜 Ver detalles de los artículos A1"):
        articulos_A1 = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"a1_{i}") for i in range(artA1)]

artA2 = st.number_input("Artículos en revistas indexadas por MINCIENCIAS A2", min_value=0, max_value=30, step=1, key="a2")
if artA2 > 0:
    with st.expander("📜 Ver detalles de los artículos A2"):
        articulos_A2 = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"a2_{i}") for i in range(artA2)]

artB = st.number_input("Artículos en revistas indexadas por MINCIENCIAS B", min_value=0, max_value=30, step=1, key="b")
if artB > 0:
    with st.expander("📜 Ver detalles de los artículos B"):
        articulos_B = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"B_{i}") for i in range(artB)]

artC = st.number_input("Artículos en revistas indexadas por MINCIENCIAS C", min_value=0, max_value=30, step=1, key="c")
if artC > 0:
    with st.expander("📜 Ver detalles de los artículos C"):
        articulos_C = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"C_{i}") for i in range(artC)]

st.write("---")

#ARTICULOS CORTOS
st.write("	Otros - Artículos Cortos")
artCA1 = st.number_input("En revistas indexadas por MINCIENCIAS A1", min_value=0, max_value=30, step=1, key="Ca1")
if artCA1 > 0:
    with st.expander("📜 Ver detalles de los artículos A1"):
        articulos_CA1 = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"Ca1_{i}") for i in range(artCA1)]

artCA2 = st.number_input("En revistas indexadas por MINCIENCIAS A2", min_value=0, max_value=30, step=1, key="Ca2")
if artCA2 > 0:
    with st.expander("📜 Ver detalles de los artículos A2"):
        articulos_CA2 = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"Ca2_{i}") for i in range(artCA2)]

artCB = st.number_input("En revistas indexadas por MINCIENCIAS B", min_value=0, max_value=30, step=1, key="Cb")
if artCB > 0:
    with st.expander("📜 Ver detalles de los artículos B"):
        articulos_CB = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"CB_{i}") for i in range(artCB)]

artCC = st.number_input("En revistas indexadas por MINCIENCIAS C", min_value=0, max_value=30, step=1, key="Cc")
if artCC > 0:
    with st.expander("📜 Ver detalles de los artículos C"):
        articulos_CC = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"CC_{i}") for i in range(artCC)]
st.write("---")

#Otros
st.write("Otros - Reportes de Casos, Revisión de Temas, Carta al Editor o Editorial")
artOA1 = st.number_input("En revistas indexadas por MINCIENCIAS A1", min_value=0, max_value=30, step=1, key="Oa1")
if artOA1 > 0:
    with st.expander("📜 Ver detalles de los artículos A1"):
        articulos_OA1 = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"Oa1_{i}") for i in range(artOA1)]

artOA2 = st.number_input("En revistas indexadas por MINCIENCIAS A2", min_value=0, max_value=30, step=1, key="Oa2")
if artOA2 > 0:
    with st.expander("📜 Ver detalles de los artículos A2"):
        articulos_OA2 = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"Oa2_{i}") for i in range(artOA2)]

artOB = st.number_input("En revistas indexadas por MINCIENCIAS B", min_value=0, max_value=30, step=1, key="Ob")
if artOB > 0:
    with st.expander("📜 Ver detalles de los artículos B"):
        articulos_OB = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"OB_{i}") for i in range(artOB)]

artOC = st.number_input("En revistas indexadas por MINCIENCIAS C", min_value=0, max_value=30, step=1, key="Oc")
if artOC > 0:
    with st.expander("📜 Ver detalles de los artículos C"):
        articulos_OC = [st.number_input(f"🔹 Artículo {i+1}",min_value=0, step=1,  key=f"OC_{i}") for i in range(artOC)]
st.write("---")

st.write("Producción de Videos Cinematográficos o Fonográficos")
dImpInt = st.number_input("Difusión de Impacto Internacional", min_value=0, max_value=30, step=1, key="d1")
if dImpInt > 0:
    with st.expander("📜 Ver detalles de Difusión de Impacto Internacional"):
        dImpInts = [st.number_input(f"🔹 Trabajo {i+1}",min_value=0, step=1,  key=f"int_{i}") for i in range(dImpInt)]

dImpNac = st.number_input("Difusión de Impacto Nacional", min_value=0, max_value=30, step=1, key="d2")
if dImpNac > 0:
    with st.expander("📜 Ver detalles de Difusión de Impacto Nacional"):
        dImpNacs = [st.number_input(f"🔹 Trabajo {i+1}",min_value=0, step=1,  key=f"nac_{i}") for i in range(dImpNac)]

st.write("---")

librosInv = st.number_input("Libros que resultan de una labor de investigación", min_value=0, max_value=30, step=1, key="librosInv")
if librosInv > 0:
    with st.expander(f"📜 Libros ({librosInv})"):
        librosInvs = [st.number_input(f"🔹 Libro {i+1} (N° de Autores):",min_value=0, step=1,  key=f"li_{i}") for i in range(librosInv)]   

librosTex = st.number_input("Libros texto", min_value=0, max_value=30, step=1, key="librosTex")
if librosTex > 0:
    with st.expander(f"📜 Libros ({librosTex})"):
        librosTexs = [st.number_input(f"🔹 Libro {i+1} (N° de Autores):",min_value=0, step=1,  key=f"Tex_{i}") for i in range(librosTex)]  

librosEn = st.number_input("Libros de ensayo", min_value=0, max_value=30, step=1, key="librosEn")
if librosEn > 0:
    with st.expander(f"📜 Libros ({librosEn})"):
        librosEns = [st.number_input(f"🔹 Libro {i+1}(N° de Autores):",min_value=0, step=1,  key=f"Ens_{i}") for i in range(librosEn)]  

librosNac = st.number_input("Premios nacionales o internacionales", min_value=0, max_value=30, step=1, key="librosNac")
if librosNac > 0:
    with st.expander(f"📜 Premios ({librosNac})"):
        librosNacs = [st.number_input(f"🔹 Premio {i+1} (N° de Autores):",min_value=0, step=1,  key=f"Nac_{i}") for i in range(librosNac)]   

patente = st.number_input("Patentes", min_value=0, max_value=30, step=1, key="Patente")
if patente > 0:
    with st.expander(f"📜 Patentes ({patente})"):
        patentes = [st.number_input(f"🔹 Patente {i+1} (N° de Autores)",min_value=0, step=1,  key=f"patentes_{i}") for i in range(patente)]   

traLib = st.number_input("Traducciones de libros", min_value=0, max_value=30, step=1, key="traLib")
if traLib > 0:
    with st.expander(f"📜 Libros: ({traLib})"):
        traLibs = [st.number_input(f"🔹 Libro {i+1} (N° de Autores)",min_value=0, step=1,  key=f"traLibs_{i}") for i in range(traLib)] 

st.write("---")

st.write("Obras Artísticas")
imTrIn = st.number_input("De impacto y trascendencia internacional", min_value=0, max_value=30, step=1, key="imTrIn")
if imTrIn > 0:
    with st.expander(f"📜 Obras: ({imTrIn})"):
        imTrIns = [st.number_input(f"🔹 Obra {i+1} (N° de Autores):",min_value=0, step=1,  key=f"imTrIns_{i}") for i in range(imTrIn)]

imTrNa = st.number_input("De impacto y trascendencia nacional", min_value=0, max_value=30, step=1, key="imTrNa")
if imTrNa > 0:
    with st.expander(f"📜 Obras: ({imTrNa})"):
        imTrNas = [st.number_input(f"🔹 Obra {i+1} (N° de Autores):",min_value=0, step=1,  key=f"imTrNas_{i}") for i in range(imTrNa)]

st.write("---")

st.write("Producción Técnica")
inTec = st.number_input("Innovación tecnológica", min_value=0, max_value=30, step=1, key="inTec")
if inTec > 0:
    with st.expander(f"📜 Trabajos: ({inTec})"):
        inTecs = [st.number_input(f"🔹 Trabajo {i+1} (N° de Autores):",min_value=0, step=1,  key=f"inTecs_{i}") for i in range(inTec)]

adTec = st.number_input("Adaptación tecnológica", min_value=0, max_value=30, step=1, key="adTec")
if adTec > 0:
    with st.expander(f"📜 Trabajos: ({adTec})"):
        adTecs = [st.number_input(f"🔹 Trabajo {i+1} (N° de Autores):",min_value=0, step=1,  key=f"adTecs_{i}") for i in range(adTec)]

st.write("---")

prSo = st.number_input("Producción de software", min_value=0, max_value=30, step=1, key="prSo")
if prSo > 0:
    with st.expander(f"📜 Trabajos: ({prSo})"):
        prSos = [st.number_input(f"🔹 Trabajo {i+1} (N° de Autores):",min_value=0, step=1,  key=f"prSos_{i}") for i in range(prSo)]







#BACKEND

def calcular_puntaje_títulos_universitarios(pregrado, clínicas, no_clínicas, maestrías, doctorados):
    puntaje_pregrado = 178 if pregrado else 0

    puntaje_clínicas = min(clínicas * 15, 75)
    puntaje_no_clínicas = no_clínicas * 20 if no_clínicas == 1 else (30 if no_clínicas >= 2 else 0)
    puntaje_maestrías = maestrías * 40 if maestrías == 1 else (60 if maestrías >= 2 else 0)
    puntaje_doctorados = doctorados * 120 if maestrías == 0 else (80 if doctorados >= 1 else 0)
    
    puntaje_postgrados = min(puntaje_clínicas + puntaje_no_clínicas + puntaje_maestrías + puntaje_doctorados, 140)

    # Si tiene Maestría y Especialización, máximo 60 puntos
    if maestrías >= 1 and no_clínicas >= 1 or clínicas >= 1:
        puntaje_postgrados = min(puntaje_postgrados, 60)


    return puntaje_pregrado+puntaje_postgrados #Máximo de Postgrado 140 puntos Si tiene Maestría y Especialización 60 puntos

#CALCULAR PUNTAJE ESCALAFON 
def Calcular_Puntaje_Escalafon_Docente(escalafone):
    escalafon_puntos = {"Auxiliar": 37, "Asistente": 58
                        , "Asociado": 74, "Titular": 96} #Puntos por escalafón
    puntaje_escalafon = escalafon_puntos.get(escalafone, 0)
    return puntaje_escalafon    

def calcular_puntaje_experiencia(e_invest, e_doc, e_dir_acad, e_no_doc, escalafons):
    # Puntos por año si la experiencia es menor a 22 años
    puntos_por_año = {
        "investigativa": 6,
        "docente": 4,
        "direccion_academica": 4,
        "no_docente": 3
    }

    # Puntos por año si la experiencia es mayor a 22 años
    puntos_por_año_mayor_22 = {
        "Auxiliar": 3,
        "Asistente": 5,
        "Asociado": 6,
        "Titular": 7,
        "Universidad Nacional de Colombia": 4
    }

    # Tope máximo de puntaje por escalafón
    tope_puntaje = {
        "Auxiliar": 20,
        "Asistente": 45,
        "Asociado": 90,
        "Titular": 120
    }

    # Cálculo de puntajes según los años de experiencia
    puntaje = 0

    if e_invest < 22:
        puntaje += e_invest * puntos_por_año["investigativa"]
    else:
        puntaje += e_invest * puntos_por_año_mayor_22[escalafons]

    if e_doc < 22:
        puntaje += e_doc * puntos_por_año["docente"]
    else:
        puntaje += e_doc * puntos_por_año_mayor_22[escalafons]

    if e_dir_acad < 22:
        puntaje += e_dir_acad * puntos_por_año["direccion_academica"]
    else:
        puntaje += e_dir_acad * puntos_por_año_mayor_22[escalafons]

    if e_no_doc < 22:
        puntaje += e_no_doc * puntos_por_año["no_docente"]
    else:
        puntaje += e_no_doc * puntos_por_año_mayor_22[escalafons]

    # Aplicar tope máximo de puntaje según escalafón
    puntaje_total_experiencia = min(puntaje, tope_puntaje[escalafons])

    return puntaje_total_experiencia


#calcular_puntaje_productividad
def ajustar_puntos(puntos, autores):
    if autores == 0:    
        return 0
    elif autores <= 3:
        return puntos
    elif 4 <= autores <= 5:
        return puntos / 2
    else:  # Más de 6 autores
        return puntos / (autores / 2)
    
# 🔹 Función auxiliar para calcular puntos ajustados por autores    
def puntaje_categorias(num_trabajos, categoria):
    if num_trabajos == 0:
       return 0
    return sum(ajustar_puntos(puntajes_base[categoria], num_autores) for num_autores in num_trabajos)

# 🔹 Función auxiliar para calcular puntos ajustados por autores
def puntaje_categoria(articulos, categoria, tipo):
    if not articulos:
        return 0
    return sum(ajustar_puntos(puntajes_base[categoria] * 0.6 if tipo=="cortos" else(puntajes_base[categoria] * 0.3 if tipo=="otros" else puntajes_base[categoria]) , num_autores) for num_autores in articulos)

def calcular_puntaje_articulos(articulos_A1, articulos_A2, articulos_B, articulos_C):
    # 🔹 Cálculo total del puntaje con el 60% aplicado
    puntaje_total = (
        puntaje_categoria(articulos_A1, "A1", "articulos") +
        puntaje_categoria(articulos_A2, "A2", "articulos") +
        puntaje_categoria(articulos_B, "B", "articulos") +
        puntaje_categoria(articulos_C, "C", "articulos")
    )

    return puntaje_total

# 🔹 Función para calcular el puntaje total de los artículos cortos

def calcular_puntaje_articulos_cortos(articulos_CA1, articulos_CA2, articulos_CB, articulos_CC):
    # 🔹 Cálculo total del puntaje con el 60% aplicado
    puntaje_total = (
        puntaje_categoria(articulos_CA1, "A1", "cortos") +
        puntaje_categoria(articulos_CA2, "A2", "cortos") +
        puntaje_categoria(articulos_CB, "B", "cortos") +
        puntaje_categoria(articulos_CC, "C", "cortos")
    )

    return puntaje_total

def calcular_puntaje_articulos_otros(articulos_OA1, articulos_OA2, articulos_OB, articulos_OC):
    # 🔹 Cálculo total del puntaje con el 30% aplicado
    puntaje_total = (
        puntaje_categoria(articulos_OA1, "A1", "otros") +
        puntaje_categoria(articulos_OA2, "A2", "otros") +
        puntaje_categoria(articulos_OB, "B", "otros") +
        puntaje_categoria(articulos_OC, "C", "otros")
    )

    return puntaje_total

def calcular_puntaje_produccion_academica(videos_int, videos_nac, libros_inv, libros_texto, libros_ensayo, 
                                          premios, patentes, traducciones, obras_int, obras_nac, 
                                          innovacion, adaptacion, software):


    # 🔹 Cálculo total del puntaje
    puntaje_total = (
        puntaje_categorias(videos_int, "videos_int") +
        puntaje_categorias(videos_nac, "videos_nac") +
        puntaje_categorias(libros_inv, "libros_inv") +
        puntaje_categorias(libros_texto, "libros_texto") +
        puntaje_categorias(libros_ensayo, "libros_ensayo") +
        puntaje_categorias(premios, "premios") +
        puntaje_categorias(patentes, "patentes") +
        puntaje_categorias(traducciones, "traducciones") +
        puntaje_categorias(obras_int, "obras_int") +
        puntaje_categorias(obras_nac, "obras_nac") +
        puntaje_categorias(innovacion, "innovacion") +
        puntaje_categorias(adaptacion, "adaptacion") +
        puntaje_categorias(software, "software")
    )

    return puntaje_total

def calcular_puntaje_productividad(articulos_A1, articulos_A2, articulos_B, articulos_C, articulos_CA1, articulos_CA2, articulos_CB, articulos_CC, articulos_OA1, articulos_OA2, articulos_OB, articulos_OC,dImpInts, dImpNacs, librosInvs, librosTexs, librosEns, librosNacs, patentes, traLibs, imTrIns, imTrNas, inTecs, adTecs, prSos):
    puntaje_total = (
        calcular_puntaje_articulos(articulos_A1, articulos_A2, articulos_B, articulos_C) +
        calcular_puntaje_articulos_cortos(articulos_CA1, articulos_CA2, articulos_CB, articulos_CC) +
        calcular_puntaje_articulos_otros(articulos_OA1, articulos_OA2, articulos_OB, articulos_OC) +
        calcular_puntaje_produccion_academica(dImpInts, dImpNacs, librosInvs, librosTexs, librosEns, librosNacs, patentes, traLibs, imTrIns, imTrNas, inTecs, adTecs, prSos)
    )

    if escalafon == "Auxiliar":
        puntaje_total = min(puntaje_total, 80)
    elif escalafon == "Asistente":
        puntaje_total = min(puntaje_total, 160)
    elif escalafon == "Asociado":
        puntaje_total = min(puntaje_total, 320)
    elif escalafon == "Titular":
        puntaje_total = min(puntaje_total, 540) 

    return puntaje_total
#BOTON CALCULAR SALARIO

if st.button("Calcular Salario"):
    puntajePosgrados = calcular_puntaje_títulos_universitarios(tipoTitulo, clinicas, noClinicas, maestrias, doctorados)
    puntaje_escalafon = Calcular_Puntaje_Escalafon_Docente(escalafon)
    puntaje_experiencia = calcular_puntaje_experiencia(eInves, eDoc, eCar, eNoDoc, escalafon)
    puntaje_productividad = calcular_puntaje_productividad(articulos_A1, articulos_A2, articulos_B, articulos_C, articulos_CA1, articulos_CA2, articulos_CB, articulos_CC, articulos_OA1, articulos_OA2, articulos_OB, articulos_OC,dImpInts, dImpNacs, librosInvs, librosTexs, librosEns, librosNacs, patentes, traLibs, imTrIns, imTrNas, inTecs, adTecs, prSos)
    
    puntaje= puntajePosgrados + puntaje_escalafon + puntaje_experiencia + puntaje_productividad
    salario = puntaje * valor_punto


    st.success(f"El puntaje total de títulos universitarios es: {puntajePosgrados}")
    st.success(f"El puntaje total del escalafón docente es: {puntaje_escalafon}")
    st.success(f"El puntaje total de experiencia calificada es: {puntaje_experiencia}")
    st.success(f"El puntaje total de productividad académica es: {puntaje_productividad}")
    st.text("---")    
    st.success(f"El puntaje total del profesor es: {puntaje}")
    st.success(f"El salario estimado es: ${salario:,.2f} COP")



