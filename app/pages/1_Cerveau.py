import streamlit as st
import time
import re
from datasets import load_dataset
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import constants

HF_TOKEN = constants.FINE_WEB_TOKEN

DATASET_NAME = "wikimedia/wikipedia"
SUBSET = "20231101.fr"
MAX_DOCS_TO_SCAN = 5000

st.set_page_config(
    page_title="Séminaire IA",
    layout="wide"
)

st.markdown("""
<style>
.highlight {
    background: #1F2937;
    padding: 0 3px;
    border-radius: 3px;
}
</style>
""", unsafe_allow_html=True)

tab_theorie, tab_demo = st.tabs(["Théorie", "Exploration"])

with tab_theorie:

    st.title("Comment naît le cerveau d'une IA")

    st.write(
        "Une intelligence artificielle apprend à partir de grands volumes de texte. "
        "Elle ne mémorise pas les phrases, mais des relations statistiques entre les mots."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Pré-entraînement")
        st.write(
            "Le modèle apprend à prédire le mot suivant dans une phrase, "
            "ce qui fait émerger des structures linguistiques."
        )
        

    with col2:
        st.subheader("Corpus")
        st.write(
            "Wikipédia, presse, documentation, code, forums et autres textes publics."
        )

with tab_demo:

    st.title("Exploration du corpus")

    query = st.text_input("Terme à rechercher", "Intelligence")

    if st.button("Lancer la recherche"):

        if not query:
            st.warning("Veuillez entrer un terme.")
            st.stop()

        pattern = re.compile(r'\b' + re.escape(query) + r'\b', re.IGNORECASE)

        ds = load_dataset(
            DATASET_NAME,
            name=SUBSET,
            split="train",
            streaming=True,
            token=HF_TOKEN
        )

        hits = 0
        scanned = 0
        start_time = time.time()

        progress_bar = st.progress(0)

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

                highlighted = (
                    snippet[:start - ctx_start]
                    + f"<span class='highlight'>{match.group(0)}</span>"
                    + snippet[end - ctx_start:]
                )

                st.write(doc.get("title", "Inconnu"))
                st.markdown(highlighted, unsafe_allow_html=True)
                st.write("---")

                if hits >= 5:
                    break

            progress_bar.progress(min(scanned / MAX_DOCS_TO_SCAN, 1.0))

            if scanned >= MAX_DOCS_TO_SCAN:
                break

        duration = time.time() - start_time

        st.write(f"Temps : {duration:.2f}s | Documents : {scanned} | Résultats : {hits}")