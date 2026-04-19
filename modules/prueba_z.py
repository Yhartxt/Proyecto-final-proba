import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def calcular(df):
    st.header("3. Prueba de Hipótesis (Prueba Z)")
    
    columnas_numericas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    columna = st.selectbox("Selecciona la variable:", columnas_numericas, key="pz_columna")
    datos = df[columna].dropna()

    mu_0 = st.number_input("Media hipotética (μ₀)", value=0.0)
    sigma = st.number_input("Desviación estándar poblacional (σ)", min_value=0.01, value=1.0)
    alpha = st.selectbox("Nivel de significancia (α)", options=[0.01, 0.05, 0.10],key="selectbox_alpha")
    tipo_prueba = st.radio("Tipo de prueba", ("Bilateral", "Unilateral Superior", "Unilateral Inferior"), key="radio_tipo_prueba")
    
    n = len(datos)
    x_barra = datos.mean()
    
    resultados = None   
    if st.button("Calcular Prueba Z"):
        
        z = (x_barra - mu_0) / (sigma / np.sqrt(n))
        
        if tipo_prueba == "Bilateral":
            p_valor = 2 * (1 - stats.norm.cdf(abs(z)))
        elif tipo_prueba == "Unilateral Superior":
            p_valor = 1 - stats.norm.cdf(z)
        else:
            p_valor = stats.norm.cdf(z)
        
        if p_valor < alpha:
            conclusion = "Rechazamos la hipótesis nula (H₀)."
        else:
            conclusion = "No rechazamos la hipótesis nula (H₀)."
        
        # Parte 4 - Mostrar resultados
        st.subheader("Resultados")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Estadístico Z", f"{z:.4f}")
        with col2:
            st.metric("p-value", f"{p_valor:.4f}")
        with col3:
            st.metric("Nivel de significancia α", f"{alpha}")

        if p_valor < alpha:
            st.error(f"Decisión falsa: {conclusion}")
        else:
            st.success(f"Decisión verdadera: {conclusion}")
        
        # Parte 5 - Grafica
        fig, ax = plt.subplots(figsize=(10, 4))
        x = np.linspace(-4, 4, 1000)
        y = stats.norm.pdf(x)
        ax.plot(x, y, 'b-', linewidth=2)

        if tipo_prueba == "Bilateral":
            z_critico = stats.norm.ppf(1 - alpha/2)
            ax.fill_between(x, y, where=(x <= -z_critico), color='red', alpha=0.4, label='Zona de rechazo')
            ax.fill_between(x, y, where=(x >= z_critico), color='red', alpha=0.4)
        elif tipo_prueba == "Unilateral Superior":
            z_critico = stats.norm.ppf(1 - alpha)
            ax.fill_between(x, y, where=(x >= z_critico), color='red', alpha=0.4, label='Zona de rechazo')
        else:
            z_critico = stats.norm.ppf(alpha)
            ax.fill_between(x, y, where=(x <= z_critico), color='red', alpha=0.4, label='Zona de rechazo')

        ax.axvline(x=z, color='green', linestyle='--', linewidth=2, label=f'Z calculado = {z:.4f}')
        ax.set_title("Curva Normal con Zona de Rechazo")
        ax.legend()
        st.pyplot(fig)
        
        return {
            "media_muestral": x_barra,
            "media_hipotetica": mu_0,
            "n": n,
            "sigma": sigma,
            "alpha": alpha,
            "tipo_prueba": tipo_prueba,
            "z": z,
            "p_valor": p_valor,
            "conclusion": conclusion
        }
    return resultados # Si no se ha presionado el botón, no regresa nada