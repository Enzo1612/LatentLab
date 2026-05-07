import streamlit as st

from transformers import pipeline


@st.cache_resource
def load_qa_model():

    return pipeline(
        "question-answering",
        model="etalab-ia/camembert-base-squadFR-fquad-piaf"
    )


qa_engine = load_qa_model()


tab_theorie, tab_demo = st.tabs([
    "Théorie",
    "Mémoire"
])


with tab_theorie:

    st.title("La fenêtre de contexte")

    st.write(
        "Les modèles de langage ne possèdent pas une mémoire infinie."
    )

    st.write(
        "Ils traitent une quantité limitée de texte à la fois : "
        "la fenêtre de contexte."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Ajout de texte")

        st.write(
            "Chaque nouveau mot est ajouté au contexte analysé par le modèle."
        )

    with col2:

        st.subheader("Limite")

        st.write(
            "Quand la fenêtre est dépassée, les informations "
            "les plus anciennes peuvent être perdues."
        )


with tab_demo:

    st.title("Test de mémoire")

    fact = st.text_input(
        "Information à retenir",
        "Le mot de passe du coffre est 1234."
    )

    question = st.text_input(
        "Question",
        "Quel est le mot de passe du coffre ?"
    )

    words_count = st.slider(
        "Nombre de mots ajoutés",
        0,
        800,
        50
    )

    if st.button("Tester"):

        with st.spinner("Analyse du contexte..."):

            filler_words = [
                "pomme",
                "oiseau",
                "arbre",
                "voiture",
                "maison",
                "soleil",
                "route",
                "chat",
                "chien",
                "livre",
                "bureau",
                "mer",
                "montagne",
                "herbe",
                "fleur"
            ]

            filler = " ".join(
                filler_words[i % len(filler_words)]
                for i in range(words_count)
            )

            full_context = f"{fact} {filler}"

            st.write(
                f"Longueur du contexte : "
                f"{len(full_context.split())} mots"
            )

            try:

                max_words = 200

                words = full_context.split()

                if len(words) > max_words:

                    context = " ".join(
                        words[-max_words:]
                    )

                    st.warning(
                        "Le début du contexte a été supprimé."
                    )

                else:

                    context = full_context

                answer = qa_engine(
                    question=question,
                    context=context
                )

                if isinstance(answer, list):
                    answer = answer[0]

                result = answer["answer"]
                score = answer["score"]

                st.subheader("Réponse")

                st.write(result)

                st.write(
                    f"Confiance : {score * 100:.1f}%"
                )

            except Exception as e:

                st.error(str(e))