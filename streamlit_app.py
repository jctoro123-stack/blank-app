import streamlit as st

st.set_page_config(
    page_title="Predicción Clínica",
    layout="wide"
)

st.title("Sistema Predictivo de Enfermedades Crónicas")
st.subheader("Atención Primaria en Salud")

st.divider()

st.header("Datos del paciente")

col1, col2 = st.columns(2)

with col1:
    edad = st.number_input("Edad", 1, 100)
    peso = st.number_input("Peso (kg)", 1.0, 200.0)
    altura = st.number_input("Altura (cm)", 50.0, 250.0)
    sistolica = st.number_input("Presión sistólica", 50, 250)

with col2:
    diastolica = st.number_input("Presión diastólica", 30, 150)
    glucosa = st.number_input("Glucosa", 50, 300)
    colesterol = st.number_input("Colesterol", 100, 400)
    fumador = st.selectbox("Fumador", ["No", "Sí"])

actividad = st.selectbox("Actividad física", ["Sí", "No"])
alcohol = st.selectbox("Consumo de alcohol", ["No", "Sí"])

if st.button("Predecir riesgo"):
    riesgo = 82

    st.divider()
    st.header("Resultado")

    if riesgo > 70:
        st.error(f"Alto riesgo: {riesgo}%")
    elif riesgo > 40:
        st.warning(f"Riesgo moderado: {riesgo}%")
    else:
        st.success(f"Bajo riesgo: {riesgo}%")

    st.subheader("Recomendación clínica")
    st.write("Se recomienda seguimiento médico prioritario.")
