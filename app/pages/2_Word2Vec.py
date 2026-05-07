import os
import streamlit as st

from gensim.models.fasttext import load_facebook_vectors
from itertools import combinations

import matplotlib.pyplot as plt


@st.cache_resource
def load_model():

    script_dir = os.path.dirname(__file__)

    model_path = os.path.join(
        script_dir,
        "..",
        "..",
        "models",
        "cc.fr.300.bin"
    )

    model_path = os.path.abspath(model_path)

    return load_facebook_vectors(model_path)


model = load_model()


tab_theorie, tab_demo, tab_vectors = st.tabs([
    "Théorie",
    "Word2Vec",
    "Vecteurs"
])


with tab_theorie:

    st.title("Comment les modèles représentent les mots")

    st.write(
        "Les modèles de langage ne manipulent pas directement du texte. "
        "Chaque mot est transformé en vecteur numérique."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Espace vectoriel")

        st.write(
            "Les mots utilisés dans des contextes similaires "
            "obtiennent des représentations proches."
        )

    with col2:

        st.subheader("Relations")

        st.write(
            "Ces vecteurs permettent de mesurer des similarités "
            "et d'effectuer des opérations mathématiques sur les mots."
        )


with tab_demo:

    st.title("Word2Vec")

    st.write(
        "Calcul vectoriel sur les représentations des mots."
    )

    col1, col2, col3 = st.columns([2, 1, 2])

    with col1:
        word1 = st.text_input("Mot 1", "roi").lower()

    with col2:
        st.write("-")

    with col3:
        word2 = st.text_input("Mot 2", "homme").lower()

    word3 = st.text_input("Mot 3", "femme").lower()

    if st.button("Calculer"):

        try:

            results = model.most_similar(
                positive=[word1, word3],
                negative=[word2],
                topn=30
            )

            input_words = {word1, word2, word3}

            filtered_results = []
            seen_words = set()

            for word, score in results:

                word_lower = word.lower()

                if not word_lower.replace("-", "").isalpha():
                    continue

                if word_lower in seen_words:
                    continue

                is_input = any(
                    word_lower == w
                    or word_lower == w + "s"
                    or word_lower == w + "x"
                    for w in input_words
                )

                if not is_input:

                    filtered_results.append((word, score))
                    seen_words.add(word_lower)

                if len(filtered_results) == 3:
                    break

            for word, score in filtered_results:

                st.write(f"{word} — {score:.2f}")

            st.divider()

            for w1, w2 in combinations(input_words, 2):

                similarity = model.similarity(w1, w2)

                st.write(
                    f"{w1} / {w2} : {similarity:.2f}"
                )

        except KeyError as e:

            st.error(f"Mot inconnu : {e}")


with tab_vectors:

    st.title("Visualisation des vecteurs")

    st.write(
        "Affichage des premières dimensions des vecteurs associés aux mots."
    )

    col1, col2 = st.columns(2)

    with col1:
        v_word1 = st.text_input("Mot A", "chien").lower()

    with col2:
        v_word2 = st.text_input("Mot B", "chat").lower()

    n_dims = st.slider(
        "Dimensions",
        10,
        100,
        30
    )

    def plot_vectors(words, n_dims):

        fig, ax = plt.subplots(figsize=(10, 4))

        for word in words:

            if word in model:

                vector = model[word][:n_dims]

                ax.plot(
                    range(n_dims),
                    vector,
                    label=word
                )

        ax.set_xlabel("Dimensions")
        ax.set_ylabel("Valeurs")

        ax.legend()

        st.pyplot(fig)

    if st.button("Afficher"):

        plot_vectors(
            [v_word1, v_word2],
            n_dims
        )