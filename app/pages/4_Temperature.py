import streamlit as st

from transformers import pipeline


tab_theorie, tab_demo = st.tabs([
    "Théorie",
    "Température"
])


with tab_theorie:

    st.title("La température")

    st.write(
        "La température modifie la distribution des probabilités "
        "utilisées pendant la génération de texte."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Température basse")

        st.write(
            "Le modèle privilégie les mots les plus probables. "
            "Le résultat est plus stable et prévisible."
        )

    with col2:

        st.subheader("Température élevée")

        st.write(
            "Les mots moins probables deviennent plus fréquents. "
            "Le résultat devient plus varié et parfois incohérent."
        )


with tab_demo:

    st.title("Comparaison")

    @st.cache_resource
    def load_generator():

        return pipeline(
            "text-generation",
            model="croissantllm/CroissantLLMBase"
        )

    generator = load_generator()

    prompt = st.text_input(
        "Début du texte",
        "Il était une fois, dans une forêt lointaine,"
    )

    tokens_to_generate = 150

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("0.2")

        if st.button("Générer", key="low"):

            with st.spinner("Génération..."):

                result = generator(
                    prompt,
                    max_new_tokens=tokens_to_generate,
                    temperature=0.2,
                    do_sample=True,
                    repetition_penalty=1.2,
                    num_return_sequences=1
                )

            st.write(result[0]["generated_text"])

    with col2:

        st.subheader("1.6")

        if st.button("Générer", key="high"):

            with st.spinner("Génération..."):

                result = generator(
                    prompt,
                    max_new_tokens=tokens_to_generate,
                    temperature=1.6,
                    do_sample=True,
                    repetition_penalty=1.2,
                    num_return_sequences=1
                )

            st.write(result[0]["generated_text"])