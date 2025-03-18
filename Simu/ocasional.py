import streamlit as st

def obtener_salario_base(categoria):
    salarios = {
        "Auxiliar de Tiempo Completo": 2645000,
        "Auxiliar de Medio Tiempo": 1509000,
        "Asistente de Tiempo Completo": 3125000,
        "Asistente de Medio Tiempo": 1749000,
        "Asociado de Tiempo Completo": 3606000,
        "Asociado de Medio Tiempo": 1990000,
        "Titular de Medio Tiempo": 2146000,
        "Titular de Tiempo Completo": 3918000
    }
    return salarios.get(categoria, 0)

def obtener_bonificacion_postgrado(nivel):
    bonificaciones = {
        "Especialización": 100000,
        "Maestría": 450000,
        "Doctorado": 900000,
        "Postdoctorado": 0
    }
    return bonificaciones.get(nivel, 0)

def obtener_bonificacion_semillero(tipo):
    bonificaciones = {
        "A1": 560000,
        "A": 470000,
        "B": 420000,
        "C": 380000,
        "Reconocidos por Colciencias": 330000,
        "Semillero": 190000
    }
    return bonificaciones.get(tipo, 0)

st.title("Cálculo de Salario Docente - Profesores ocasionales (acuerdo 006 de 2018)")

# Entrada de datos con selectbox
categoria = st.selectbox("Seleccione la categoría del docente:",
    ["Auxiliar de Tiempo Completo", "Auxiliar de Medio Tiempo", "Asistente de Tiempo Completo",
     "Asistente de Medio Tiempo", "Asociado de Tiempo Completo", "Asociado de Medio Tiempo",
     "Titular de Medio Tiempo", "Titular de Tiempo Completo"])

postgrado = st.selectbox("Seleccione el nivel de postgrado:",
    ["Especialización", "Maestría", "Doctorado", "Postdoctorado"])

semillero = st.selectbox("Seleccione la categoría de semillero:",
    ["A1", "A", "B", "C", "Reconocidos por Colciencias", "Semillero"])

if categoria and postgrado and semillero:
    if st.button("Calcular Salario"):
        salario_base = obtener_salario_base(categoria)
        bonificacion_postgrado = obtener_bonificacion_postgrado(postgrado)
        bonificacion_semillero = obtener_bonificacion_semillero(semillero)
        salario_total = salario_base + bonificacion_postgrado + bonificacion_semillero
        
        st.write("### Resultados")
        st.success(f"Salario Base: ${salario_base:,.2f} COP")
        st.success(f"Bonificación por Postgrado: ${bonificacion_postgrado:,.2f} COP")
        st.success(f"Bonificación por Semillero: ${bonificacion_semillero:,.2f} COP")
        st.success(f"Salario Total del Profesor: ${salario_total:,.2f} COP")
else:
    st.warning("Debe seleccionar una opción en cada categoría para calcular el salario.")
