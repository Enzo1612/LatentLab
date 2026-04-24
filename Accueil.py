import streamlit as st

st.set_page_config(page_title="LatentLab", page_icon="🤖", layout="centered")

# Massive, clean header
st.markdown("<h1 style='text-align: center; font-size: 3.5rem;'>LatentLab</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>Dans le Cerveau d'une Intelligence Artificielle</h3>", unsafe_allow_html=True)

st.write("")
st.write("")

# Visual Navigation Grid
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/10_La_Theorie_Des_Mots.py", label="1. Le Découpage (Tokens)", icon="✂️")
    st.page_link("pages/21_Le_Cerveau.py", label="2. Les Probabilités", icon="🎲")
    st.page_link("pages/31_La_Température.py", label="3. La Créativité", icon="🌡️")

with col2:
    st.page_link("pages/41_La_Mémoire.py", label="4. La Mémoire", icon="📚")
    st.page_link("pages/51_L_Apprentissage.py", label="5. L'Entraînement", icon="📉")
    st.page_link("pages/61_Les_Hallucinations.py", label="6. Les Mensonges", icon="👻")

st.divider()
st.info("💡 **Mission :** Découvrir pourquoi l'IA a l'air intelligente, et comment la piéger.")