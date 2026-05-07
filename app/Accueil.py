import streamlit as st

st.set_page_config(
    page_title="Démo Séminaire IA",
    layout="wide"
)

st.markdown(
    """
    <style>
    #MainMenu, header, footer {visibility: hidden;}

    .block-container {
        padding-top: 2rem;
    }

    h1, h2, h3 {
        cursor: default;
        user-select: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("LatentLab")

st.subheader("Séminaire interactif sur les modèles de langage")

st.write(
    "Exploration des mécanismes fondamentaux des modèles de langage : "
    "pré-entraînement, représentations vectorielles, génération probabiliste et mémoire contextuelle."
)

st.divider()

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.subheader("Le Cerveau Géant")
    st.page_link(
        "pages/1_Cerveau.py",
        label="Exploration du corpus utilisé pendant le pré-entraînement"
    )

with col2:
    st.subheader("Word2Vec")
    st.page_link(
        "pages/2_Word2Vec.py",
        label="Représentation mathématique du sens des mots"
    )

with col3:
    st.subheader("Le Prochain Mot")
    st.page_link(
        "pages/3_Prochain_Mot.py",
        label="Prédiction probabiliste du token suivant"
    )

st.divider()

col4, col5, col6 = st.columns(3, gap="large")

with col4:
    st.subheader("La Température")
    st.page_link(
        "pages/4_Temperature.py",
        label="Contrôle de l’aléatoire du modèle"
    )

with col5:
    st.subheader("Limite de Mémoire")
    st.page_link(
        "pages/5_Memoire_Courte.py",
        label="Fenêtre de contexte et saturation"
    )

with col6:
    pass