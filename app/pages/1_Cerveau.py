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

tab_theorie, tab_demo = st.tabs(["📖 Théorie : La Bibliothèque", "⚙️ Expérience Interactive"])

with tab_theorie:
    st.title("Comment naît le cerveau d'une IA ?")
    
    st.markdown("""
    <div style='background-color: #141B2D; padding: 30px; border-radius: 15px; border: 1px solid #00E5FF; text-align: center;'>
        <h2 style='color: #00E5FF;'>L'Entraînement de la Machine</h2>
        <p style='font-size: 20px; line-height: 1.6;'>
            Une IA n'a <strong>ni idée</strong> ni conscience humaine. Lors de sa naissance, elle va ingurgiter la quasi-totalité de l'internet humain dans son "Cerveau".<br><br>
        </p>
        <div style='display: flex; justify-content: space-around; margin-top: 30px;'>
            <div style='background-color: rgba(0, 229, 255, 0.1); padding: 20px; border-radius: 10px; width: 45%;'>
                <h3>📚 La Bibliothèque Géante</h3>
                <p>Pour la langue française, l'IA a dévoré toute l'encyclopédie Wikipédia, la Base de lois, et toutes les pages web publiques.</p>
            </div>
            <div style='background-color: rgba(255, 100, 100, 0.1); padding: 20px; border-radius: 10px; width: 45%;'>
                <h3>🧠 L'Effet Éponge</h3>
                <p>L'IA ne fait pas de Copier/Coller. Elle "compresse" les livres en concepts mathématiques pour y déceler des règles de grammaire et des liens logiques.</p>
            </div>
        </div>
    </div>
    <br>
    <p style='text-align: center; color: gray;'><em>(Passez à l'onglet Expérience Interactive en haut 👆 pour plonger dans les données)</em></p>
    """, unsafe_allow_html=True)

with tab_demo:
    st.title("1. Explorer les Données d'Entraînement")
    st.write("Naviguons en direct dans la base de Wikipédia ingérée par le modèle pendant son entraînement (le pre-training) !")

    query = st.text_input("Cherchez une idée profondément enfouie dans la base :", "Intelligence")

    if st.button("Plonger dans la Mémoire Morte de l'IA"):
        if not query:
            st.warning("Veuillez entrer un mot à chercher.")
            st.stop()
            
        st.write(f"Vérification du corpus brut ({DATASET_NAME})...")

        try:
            pattern = re.compile(r'\b' + re.escape(query) + r'\b', re.IGNORECASE)
        except Exception as e:
            st.error(f"Erreur de recherche: {e}")
            st.stop()

        try:
            # Streaming=True évite que la machine de votre séminaire ne télécharge les 25 Go de données !
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

                # Mise en évidence du texte trouvé avec la couleur Ciel du nouveau thème sombre !
                snippet_html = f"...{snippet[:start-ctx_start]}<span style='background-color:#00E5FF; color:black; font-weight:bold; padding:2px 4px; border-radius:3px;'>{match.group(0)}</span>{snippet[end-ctx_start:]}..."

                with results_container:
                    st.markdown(f"**Archive : {doc.get('title', 'Inconnu')}**")
                    st.markdown(snippet_html, unsafe_allow_html=True)
                    st.divider()
                    
                if hits >= 5: # On s'arrête après 5 trouvailles pour la présentation
                    break

            progress_bar.progress(min(scanned / MAX_DOCS_TO_SCAN, 1.0))
            status_text.text(f"Archives traitées : {scanned} | Traces détectées : {hits}")

            if scanned >= MAX_DOCS_TO_SCAN:
                break

        duration = time.time() - start_time

        st.success("Recherche terminée !")
        st.write(f"⏱️ Temps de calcul : {duration:.2f}s | 📄 Fichiers balayés : {scanned} | 🎯 Éclats récupérés : {hits}")


