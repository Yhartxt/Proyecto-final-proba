import streamlit as st
import os
from dotenv import load_dotenv
from modules import carga_datos, visualizacion, prueba_z, asistente_ia #Aqui se importan los modulos si se mueve algo valio queso

st.set_page_config(page_title="App de Estadística", layout="wide")

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
st.title("Proyecto de Probabilidad y Estadística")

#Carga de Datos
df = carga_datos.obtener_datos()

if df is not None:
    st.session_state["df"] = df

if "df" in st.session_state:
    df = st.session_state["df"]
    
    visualizacion.mostrar_graficas(df)  
    resultados_z = prueba_z.calcular(df)

    if resultados_z is not None:
        st.session_state["resultados_z"] = resultados_z

    if "resultados_z" in st.session_state:
        asistente_ia.consultar_gemini(st.session_state["resultados_z"], api_key)
    else:
        st.info("Configura y ejecuta la Prueba Z para habilitar el asistente de IA.")
    
else:
    st.info("Sube un archivo o genera datos para comenzar.")