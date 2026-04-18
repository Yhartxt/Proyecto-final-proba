import streamlit as st
import os
from dotenv import load_dotenv
from modules import carga_datos, visualizacion, prueba_z, asistente_ia #Aqui se importan los modulos si se mueve algo valio queso
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
st.set_page_config(page_title="App de Estadística", layout="wide")
st.title("Proyecto de Probabilidad y Estadística")
#Carga de Datos
df = carga_datos.obtener_datos()
if df is not None:
    visualizacion.mostrar_graficas(df)
    resultados_z = prueba_z.calcular(df)
    asistente_ia.consultar_gemini(resultados_z, api_key)
else:
    st.info("Sube un archivo para comenzar.")