import streamlit as st

st.set_page_config(page_title="Démo Séminaire IA", page_icon="�", layout="wide")
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.stApp {
    # background-image: url("./assets/home_background.jpg");
    # background-size: cover;
}
/* Style pour arrondir davantage les boites et moderniser les boutons */
div.stButton > button {
    border-radius: 20px;
    font-weight: bold;
    border: 1px solid #00E5FF;
}
/* Ajout de styles pour les cartes cliquables (hover effect) */
.module-card {
    background-color: rgba(20, 27, 45, 0.7); 
    padding: 10px; 
    border-radius: 15px; 
    height: 175px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.module-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
}
a.card-link {
    text-decoration: none;
    color: inherit;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; padding: 15px 10px; background: linear-gradient(135deg, #0A0E17 0%, #141B2D 100%); border-radius: 20px; border-bottom: 2px solid #00E5FF; margin-bottom: 40px;'>
    <h1 style='font-size: 3em; color: #F0F2F6; margin-bottom: 20px; font-weight: 800;'>Latent<span style='color: #00E5FF;'>Lab</span> 🧬</h1>
    <h3 style='color: #8A9BA8; font-weight: 400;'>Séminaire Interactif de Découverte de l'IA pour les Collégiens</h3>
    <p style='color: #A0B0C0; max-width: 800px; margin: 20px auto 0 auto; font-size: 1.1em;'>
        Explorez le "cerveau" des Intelligences Artificielles en temps réel ! <br>À travers 5 expériences visuelles, nous allons casser la magie et comprendre la logique mathématique qui se cache derrière ChatGPT.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <a href="Le_Cerveau_Geant" target="_self" class="card-link">
        <div class="module-card" style='border-left: 4px solid #FF5050;'>
            <h3 style='margin-top: 0;'>1️⃣ Le Cerveau Géant</h3>
            <p style='color: #A0B0C0;'>Visualisation de l'immense base de données (Wikipédia) que l'IA a dû avaler avant même de dire son premier mot.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="Word2Vec" target="_self" class="card-link">
        <div class="module-card" style='border-left: 4px solid #00E5FF;'>
            <h3 style='margin-top: 0;'>2️⃣ Word2Vec</h3>
            <p style='color: #A0B0C0;'>Comment l'IA additionne et soustrait le <em>sens</em> des mots par les mathématiques.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)


with col3:
    st.markdown("""
    <a href="Prochain_Mot" target="_self" class="card-link">
        <div class="module-card" style='border-left: 4px solid #B000FF;'>
            <h3 style='margin-top: 0;'>3️⃣ Le Prochain Mot</h3>
            <p style='color: #A0B0C0;'>L'IA ne réfléchit pas à la phrase entière, elle devine juste le prochain jeton à l'aide de probabilités.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col4, col5, col6 = st.columns([1, 2, 2])

with col5:
    st.markdown("""
    <a href="Temperature" target="_self" class="card-link">
        <div class="module-card" style='border-left: 4px solid #FFC300;'>
            <h3 style='margin-top: 0;'>4️⃣ La Température</h3>
            <p style='color: #A0B0C0;'>Comment un seul curseur mathématique transforme une machine logique en un poète complètement fou.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <a href="Memoire_Courte" target="_self" class="card-link">
        <div class="module-card" style='border-left: 4px solid #00FF88;'>
            <h3 style='margin-top: 0;'>5️⃣ Limite de Mémoire</h3>
            <p style='color: #A0B0C0;'>Test en direct de la limite stricte de la mémoire vive : que se passe-t-il si on lui donne un document trop grand ?</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

st.stop()

