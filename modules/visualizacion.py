import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import scipy.stats as stats

def mostrar_graficas(df):
    st.header("2. Visualización de Distribuciones")
    
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    if not columnas_numericas:
        st.warning("Tu archivo no contiene columnas numéricas.")
        return
        
    columna_seleccionada = st.selectbox("Selecciona la variable a analizar:", columnas_numericas,key="viz_columna")
    datos = df[columna_seleccionada].dropna()
    
    #Crea dos columnas en la pantalla para poner las gráficas lado a lado
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Histograma y KDE")
        fig_hist, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(datos, kde=True, ax=ax, color="skyblue")
        ax.set_title("Forma de la distribución")
        st.pyplot(fig_hist)
        
    with col2:
        st.subheader("Boxplot (Atípicos)")
        fig_box = px.box(df, y=columna_seleccionada, points="outliers", 
                         title="Detección de Outliers")
        st.plotly_chart(fig_box, use_container_width=True)

    st.markdown("### Análisis de los Datos")
    
    #Cálculo del sesgo 
    sesgo = datos.skew()
    if abs(sesgo) < 0.5:
        texto_sesgo = "La distribución es **Simétrica** (bajo sesgo)."
    elif sesgo > 0:
        texto_sesgo = "Hay **Sesgo Positivo** (cola hacia la derecha)."
    else:
        texto_sesgo = "Hay **Sesgo Negativo** (cola hacia la izquierda)."
        
    stat, p_valor = stats.shapiro(datos)
    if p_valor > 0.05:
        texto_normal = "La distribución **SÍ parece Normal**."
    else:
        texto_normal = "La distribución **NO parece Normal**."

    #Muestra de resultados
    st.info(f"**¿La distribución parece normal?** {texto_normal} (p-value: {p_valor:.3f})")
    st.info(f"**¿Hay sesgo?** {texto_sesgo} (Valor de asimetría: {sesgo:.2f})")
    st.info("**¿Hay outliers?** Revisa el Boxplot interactivo. Si ves puntos sueltos fuera de los 'bigotes', esos son tus outliers.")