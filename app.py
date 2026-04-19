import streamlit as st
import os
from dotenv import load_dotenv
from modules import carga_datos, visualizacion, prueba_z, asistente_ia #Aqui se importan los modulos si se mueve algo valio queso

st.set_page_config(page_title="App de Estadística", layout="wide")

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
st.set_page_config(page_title="App de Estadística", layout="wide")
st.title("Proyecto de Probabilidad y Estadística")
#Carga de Datos
df = carga_datos.obtener_datos()

if df is not None:
    st.session_state["df"] = df
if "df" in st.session_state:
    df = st.session_state["df"]
else:
    st.info("Sube un archivo o genera datos para comenzar.")