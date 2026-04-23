import streamlit as st
from groq import Groq

def consultar_gemini(resultados, api_key):
    if not resultados:
        return

    st.header("4. Asistente de IA (Interpretación)")
    
    if not api_key:
        st.error("⚠️ No se encontró la API Key. Asegúrate de que esté en tu archivo .env")
        return

    cliente = Groq(api_key=api_key)

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
    los supuestos de la prueba son razonables. No devuelvas código, solo la explicación.
    """

    st.write("¿Tienes dudas sobre los resultados? Pídele a la IA que te los explique.")
    if st.button("✨ Preguntarle a la IA"):
        with st.spinner("La IA está analizando los datos..."):
            try:
                respuesta = cliente.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile",
                )
                st.markdown("### 🤖 Análisis de la IA")
                st.info(respuesta.choices[0].message.content)
            except Exception as e:
                st.error(f"Hubo un problema al conectar con la API: {e}")