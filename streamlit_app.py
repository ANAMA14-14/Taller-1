import streamlit as st
from datetime import datetime

# Estado inicial
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}
if "messages" not in st.session_state:
    st.session_state.messages = []

responses = {
    "solicitar_nombre": "📝 Por favor dime tu **primer nombre**.",
    "solicitar_categoria": "✅ Hola {nombre}, escribe la categoría de tu PQRS.",
    "solicitar_detalle": "👍 Entendido, ahora detalla tu PQRS.",
    "confirmacion_final": "🎉 ¡Hemos recibido tu PQRS! Un agente se comunicará pronto."
}

# Mostrar historial
st.title("🤖 Asistente Meeiko")

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Flujo PQRS
    if st.session_state.step == 0:
        response = responses["solicitar_nombre"]
        st.session_state.step = 1

    elif st.session_state.step == 1:
        st.session_state.data["nombre"] = prompt
        response = responses["solicitar_categoria"].format(nombre=prompt)
        st.session_state.step = 2

    elif st.session_state.step == 2:
        st.session_state.data["categoria"] = prompt
        response = responses["solicitar_detalle"]
        st.session_state.step = 3

    elif st.session_state.step == 3:
        st.session_state.data["detalle"] = prompt
        response = responses["confirmacion_final"]
        st.session_state.step = 0
        st.session_state.data = {}

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
