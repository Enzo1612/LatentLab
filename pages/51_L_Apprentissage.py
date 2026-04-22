import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="L'Apprentissage", page_icon="📉")

st.title("Étape 5 : L'Apprentissage")
st.markdown("> **L'IA naît ignorante. Elle devient intelligente en réduisant ses erreurs.**")
st.write("Démonstration : L'entraînement de l'IA (La descente de gradient).")

# 1. State Management: The AI's "Brain"
# Streamlit reruns the script top-to-bottom on every click. 
# session_state keeps our data alive across those reruns.
if "epoch" not in st.session_state:
    st.session_state.epoch = 0
    st.session_state.error = 100.0  # Starts 100% wrong
    st.session_state.history = [100.0]

st.info("Au début, l'IA se trompe complètement. Clique pour l'entraîner cycle par cycle.")

# 2. The Training Loop (Button)
if st.button("Entraîner l'IA"):
    if st.session_state.error > 1.0:
        st.session_state.epoch += 1
        
        # We simulate optimization: the error drops by 10% to 40% each click.
        # It's an exponential decay, mimicking real loss curves.
        reduction = st.session_state.error * random.uniform(0.1, 0.4)
        st.session_state.error -= reduction
        st.session_state.history.append(st.session_state.error)

# 3. The Metrics Display
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Cycles d'entraînement", value=st.session_state.epoch)
with col2:
    # We round the error to 1 decimal place for clean UI
    st.metric(label="Taux d'Erreur", value=f"{st.session_state.error:.1f}%")

st.divider()

# 4. The Loss Curve Visualization
st.subheader("La Courbe d'Apprentissage (Loss Curve) :")
chart_data = pd.DataFrame(st.session_state.history, columns=["Erreur (%)"])
# Streamlit's native line chart is perfect for this
st.line_chart(chart_data)

# 5. The Victory State
if st.session_state.error <= 5.0:
    st.success("Entraînement terminé ! L'erreur est proche de zéro, le modèle est optimisé.")
    
    # A button to reset the session_state and start over
    if st.button("Réinitialiser le cerveau"):
        st.session_state.clear()
        st.rerun()