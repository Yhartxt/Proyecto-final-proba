import streamlit as st
import pandas as pd
import numpy as np

def obtener_datos():
    """
    Esta función maneja la barra lateral para que el usuario suba su CSV
    o genere datos de prueba aleatorios.
    """
    st.sidebar.header("1. Carga de Datos")  
    
    opcion = st.sidebar.radio(
        "¿Cómo deseas obtener los datos?", 
        ("Subir archivo CSV", "Generar datos sintéticos")
    )

    df = None 
    if opcion == "Subir archivo CSV":
        # Opción A: Cargar archivo
        archivo_subido = st.sidebar.file_uploader("Sube tu archivo CSV aquí", type=["csv"])
        
        if archivo_subido is not None:
            df = pd.read_csv(archivo_subido)
            st.sidebar.success("¡Archivo cargado correctamente!")
            
    else:
        # Opción B: Generar datos sintéticos
        st.sidebar.subheader("Parámetros de los datos")
        
        n_muestras = st.sidebar.slider("Tamaño de la muestra (n)", min_value=1, max_value=1000, value=100)
        media_deseada = st.sidebar.number_input("Media aproximada", value=50.0)
        desviacion = st.sidebar.number_input("Desviación estándar", value=15.0)
        if n_muestras <30:
            st.sidebar.warning("El tamaño de la muestra debe ser al menos 30 para cumplir con los requisitos del proyecto.")
            
        if st.sidebar.button("Generar Datos"):
            datos_aleatorios = np.random.normal(loc=media_deseada, scale=desviacion, size=n_muestras)
            
            df = pd.DataFrame({"Valor": datos_aleatorios}) 
            st.session_state["df"] = df
            st.sidebar.success("¡Datos sintéticos generados!")

    return df