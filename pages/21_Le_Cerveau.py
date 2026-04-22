import streamlit as st

st.set_page_config(page_title="Le Moteur Statistique", page_icon="🧠")

st.title("Étape 2 : Le Moteur Statistique")
st.markdown("> **L'IA ne réfléchit pas. Elle calcule des probabilités.**")
st.write("Démonstration : L'IA classe les prochains mots possibles avec un pourcentage.")

knowledge_base = {
    "Christophe Colomb a découvert...": {
        "l'Amérique": 98, 
        "la lune": 1, 
        "une pizza": 1
    },
    "Le chat boit du...": {
        "lait": 95, 
        "café": 4, 
        "jus de pomme": 1
    }
}

selected_sentence = st.selectbox("Choisis un début de phrase :", list(knowledge_base.keys()))

st.subheader("Ce que l'IA prédit pour la suite :")

predictions = knowledge_base[selected_sentence]

for word, probability in predictions.items():
    # We use columns to align the text and the progress bar nicely
    col1, col2 = st.columns([1, 3]) 
    
    with col1:
        st.write(f"**{word}** ({probability}%)")
    with col2:
        st.progress(probability)