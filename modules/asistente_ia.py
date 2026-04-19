import streamlit as st
import google.generativeai as genai

def consultar_gemini(resultados, api_key):
    """
    Este módulo toma los resultados de la prueba Z y le pide a Gemini
    que los interprete como un experto en estadística.
    """
    if not resultados:
        return # Si el usuario aún no presiona "Calcular Prueba Z", no hacemos nada

    st.header("4. Asistente de IA (Interpretación)")
    
    if not api_key:
        st.error("⚠️ No se encontró la API Key. Asegúrate de que esté en tu archivo .env")
        return

    genai.configure(api_key=api_key)
    
    modelo = genai.GenerativeModel('gemini-2.0-flash')
    
    prompt = f"""
    Se realizó una prueba Z con los siguientes parámetros:
    - media muestral = {resultados['media_muestral']:.4f}
    - media hipotética = {resultados['media_hipotetica']}
    - n = {resultados['n']}
    - sigma = {resultados['sigma']}
    - alpha = {resultados['alpha']}
    - tipo de prueba = {resultados['tipo_prueba']}

    El estadístico Z fue = {resultados['z']:.4f} y el p-value fue {resultados['p_valor']:.4f}.
    La decisión de la app fue: {resultados['conclusion']}

    ¿Se rechaza H0? Explica la decisión de forma clara pero profesional, y comenta si 
    los supuestos de la prueba (como tamaño de muestra >= 30 y varianza poblacional conocida) 
    son razonables en este caso. No devuelvas código, solo la explicación.
    """

    st.write("¿Tienes dudas sobre los resultados? Pídele a la IA que te los explique.")
    if st.button("✨ Preguntarle a Gemini"):
        with st.spinner("Gemini está analizando los datos..."):
            try:
                respuesta = modelo.generate_content(prompt)
                
                st.markdown("### 🤖 Análisis de la IA")
                st.info(respuesta.text)
                
            except Exception as e:
                st.error(f"Hubo un problema al conectar con la API: {e}")