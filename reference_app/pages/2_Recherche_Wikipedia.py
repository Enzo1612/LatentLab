import streamlit as st
import time
import re
from datasets import load_dataset
import sys
import os

# Ajout du dossier parent au path pour pouvoir importer constants
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import constants

HF_TOKEN = constants.FINE_WEB_TOKEN

DATASET_NAME = "wikimedia/wikipedia"
SUBSET = "20231101.fr"
MAX_DOCS_TO_SCAN = 5000  # Réduit pour la démo

st.title("2. Explorer le cerveau de l'IA")
st.write("L'IA apprend en lisant des milliards de textes. Cherchons dans un grand corpus Wikipédia français en direct !")

query = st.text_input("Quel mot ou concept voulez-vous chercher ?", "Intelligence")

if st.button("Chercher dans le cerveau du modèle"):
    if not query:
        st.warning("Veuillez entrer un mot à chercher.")
        st.stop()
        
    st.write(f"Connexion à la base de données {DATASET_NAME}...")

    try:
        pattern = re.compile(r'\b' + re.escape(query) + r'\b', re.IGNORECASE)
    except Exception as e:
        st.error(f"Erreur de recherche: {e}")
        st.stop()

    try:
        ds = load_dataset(
            DATASET_NAME,
            name=SUBSET,
            split="train",
            streaming=True,
            token=HF_TOKEN
        )
    except Exception as e:
        st.error(f"Erreur de connexion: {e}")
        st.stop()

    hits = 0
    scanned = 0
    start_time = time.time()

    progress_bar = st.progress(0)
    status_text = st.empty()
    results_container = st.container()

    for doc in ds:
        scanned += 1
        text = doc["text"]

        match = pattern.search(text)
        if match:
            hits += 1

            start, end = match.span()
            ctx_start = max(0, start - 80)
            ctx_end = min(len(text), end + 80)
            snippet = text[ctx_start:ctx_end].replace("\n", " ")

            snippet_html = f"...{snippet[:start-ctx_start]}<span style='background-color:#ffeb3b; color:black; font-weight:bold; padding:2px;'>{match.group(0)}</span>{snippet[end-ctx_start:]}..."

            with results_container:
                st.markdown(f"**Article : {doc.get('title', 'Inconnu')}**")
                st.markdown(snippet_html, unsafe_allow_html=True)
                st.divider()
                
            if hits >= 5: # On s'arrête après 5 trouvailles pour la présentation
                break

        progress_bar.progress(min(scanned / MAX_DOCS_TO_SCAN, 1.0))
        status_text.text(f"Documents analysés : {scanned} | Trouvailles : {hits}")

        if scanned >= MAX_DOCS_TO_SCAN:
            break

    duration = time.time() - start_time

    st.success("Recherche terminée !")
    st.write(f"⏱️ Temps: {duration:.2f}s | 📄 Articles lus : {scanned} | 🎯 Correspondances affichées : {hits}")

