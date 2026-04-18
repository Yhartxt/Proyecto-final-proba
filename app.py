import streamlit as st
import os
from dotenv import load_dotenv
# Importamos TUS módulos (los archivos que crearás)
from modules import carga_datos, visualizacion, prueba_z, asistente_ia
# Cargamos la llave de Gemini
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
st.set_page_config(page_title="App de Estadística", layout="wide")
st.title("📊 Proyecto de Probabilidad y Estadística")
# 1. Módulo de Carga de Datos
df = carga_datos.obtener_datos()
if df is not None:
    # 2. Módulo de Visualización
    visualizacion.mostrar_graficas(df)

    # 3. Módulo de Prueba Z
    resultados_z = prueba_z.calcular(df)

    # 4. Módulo de IA
    asistente_ia.consultar_gemini(resultados_z, api_key)
else:
    st.info("Sube un archivo para comenzar.")