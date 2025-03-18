import streamlit as st
import random

def calcular_nomina(profesores, salarios, beneficios):
    total_nomina = 0
    total_beneficios = 0
    detalles = []
    for categoria, cantidad in profesores.items():
        salario = salarios.get(categoria, 0)
        beneficio = beneficios.get(categoria, 0)
        subtotal = cantidad * salario
        subtotal_beneficio = cantidad * beneficio
        detalles.append(f"{categoria}: {cantidad} docentes x ${salario:,.0f} + Beneficio: ${beneficio:,.0f} = ${subtotal + subtotal_beneficio:,.0f}")
        total_nomina += subtotal
        total_beneficios += subtotal_beneficio
    return detalles, total_nomina, total_beneficios

def generar_productividad():
    return {
        "Artículos en revistas indexadas": random.randint(2, 10),
        "Libros publicados": random.randint(0, 3),
        "Capítulos de libros": random.randint(0, 5),
        "Patentes registradas": random.randint(0, 2)
    }

# Definición de salarios y beneficios según la categoría
salarios_ocacionales = {
    "Auxiliar de Tiempo Completo": 2645000,
    "Auxiliar de Medio Tiempo": 1509000,
    "Asistente de Tiempo Completo": 3125000,
    "Asistente de Medio Tiempo": 1749000,
    "Asociado de Tiempo Completo": 3606000,
    "Asociado de Medio Tiempo": 1990000,
    "Titular de Medio Tiempo": 2146000,
    "Titular de Tiempo Completo": 3918000,
}

salarios_planta = {
    "Auxiliar": 3000000,
    "Asistente": 4000000,
    "Asociado": 5000000,
    "Titular": 6000000,
}

beneficios_planta = {key: val * 0.2 for key, val in salarios_planta.items()}  # 20% adicional en beneficios
beneficios_ocacionales = {key: val * 0.1 for key, val in salarios_ocacionales.items()}  # 10% adicional en beneficios

st.title("Simulador de Nómina y Productividad Docente")

st.header("Docentes de Planta")
profesores_planta = {}
for categoria in salarios_planta.keys():
    profesores_planta[categoria] = st.number_input(f"Cantidad de {categoria}s", min_value=0, step=1)

st.header("Docentes Ocasionales")
profesores_ocacionales = {}
for categoria in salarios_ocacionales.keys():
    profesores_ocacionales[categoria] = st.number_input(f"Cantidad de {categoria}s", min_value=0, step=1)

if st.button("Calcular Nómina y Productividad"):
    detalles_planta, total_planta, beneficios_planta = calcular_nomina(profesores_planta, salarios_planta, beneficios_planta)
    detalles_ocacionales, total_ocacionales, beneficios_ocacionales = calcular_nomina(profesores_ocacionales, salarios_ocacionales, beneficios_ocacionales)
    total_general = total_planta + total_ocacionales
    total_beneficios = beneficios_planta + beneficios_ocacionales
    
    st.subheader("Resumen de Nómina")
    st.write("### Planta")
    for detalle in detalles_planta:
        st.write(detalle)
    st.write(f"**Total Salarios Planta: ${total_planta:,.0f}**")
    st.write(f"**Total Beneficios Planta: ${beneficios_planta:,.0f}**")
    
    st.write("### Ocasionales")
    for detalle in detalles_ocacionales:
        st.write(detalle)
    st.write(f"**Total Salarios Ocasionales: ${total_ocacionales:,.0f}**")
    st.write(f"**Total Beneficios Ocasionales: ${beneficios_ocacionales:,.0f}**")
    
    st.write(f"## **Total General (Salarios + Beneficios): ${total_general + total_beneficios:,.0f}**")
    
    # Simulación de productividad académica
    productividad = generar_productividad()
    st.subheader("Productividad Académica Promedio")
    for key, value in productividad.items():
        st.write(f"**{key}:** {value}")