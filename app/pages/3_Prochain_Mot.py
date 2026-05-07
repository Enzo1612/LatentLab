import streamlit as st
import torch

from transformers import AutoModelForCausalLM, AutoTokenizer

import matplotlib.pyplot as plt


@st.cache_resource
def load_hf_model():

    model_name = "croissantllm/CroissantLLMBase"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModelForCausalLM.from_pretrained(model_name)

    return tokenizer, model


tokenizer, model = load_hf_model()


tab_theorie, tab_demo = st.tabs([
    "Théorie",
    "Prédiction"
])


with tab_theorie:

    st.title("Prédiction du prochain mot")

    st.write(
        "Les modèles génératifs produisent du texte en prédisant "
        "le token suivant à partir du contexte précédent."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Probabilités")

        st.write(
            "Le modèle attribue une probabilité à chaque mot possible "
            "du vocabulaire."
        )

    with col2:

        st.subheader("Génération")

        st.write(
            "Le texte est généré token après token "
            "par échantillonnage des probabilités."
        )


with tab_demo:

    st.title("Prédiction")

    sentence = st.text_input(
        "Phrase",
        "L'explorateur Christophe Colomb est célèbre pour avoir découvert l'"
    )

    if st.button("Calculer"):

        with st.spinner("Calcul des probabilités..."):

            inputs = tokenizer(
                sentence,
                return_tensors="pt"
            )

            with torch.no_grad():

                outputs = model(**inputs)

        next_token_logits = outputs.logits[0, -1, :]

        next_token_probs = torch.nn.functional.softmax(
            next_token_logits,
            dim=-1
        )

        top_probs, top_indices = torch.topk(
            next_token_probs,
            100
        )

        stop_words = {
            "le", "la", "les", "l", "un", "une", "des", "d", "de", "du",
            "à", "au", "aux", "ce", "cet", "cette", "ces",
            "et", "en", "ou", "où", "par", "pour", "dans", "sur",
            "avec", "sans", "sous", "vers", "qui", "que", "qu",
            "il", "elle", "on", "nous", "vous", "ils", "elles",
            "je", "tu", "y", "est", "sont", "a", "ont",
            "ne", "pas", "plus", "jamais",
            "the", "a", "an", "that", "this", "to", "of", "and", "in"
        }

        labels = []
        values = []

        for prob, idx in zip(top_probs, top_indices):

            word = tokenizer.decode([idx.item()]).strip()

            word_clean = word.lower().replace("'", "")

            if (
                len(word_clean) > 1
                and word_clean.isalpha()
                and word_clean not in stop_words
            ):

                labels.append(word)
                values.append(prob.item())

            if len(labels) == 5:
                break

        if not labels:

            labels = [
                tokenizer.decode([idx.item()]).strip()
                for idx in top_indices[:5]
            ]

            values = top_probs[:5].tolist()

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.bar(
            labels,
            [v * 100 for v in values]
        )

        ax.set_ylabel("Probabilité (%)")

        st.pyplot(fig)