import streamlit as st
from transformers import pipeline

st.title("4. La Température (La Créativité) 🌡️")
st.write("Si la température est à 0, l'IA est mathématique et logique. Si elle monte, l'IA devient créative... ou folle !")

@st.cache_resource
def load_generator():
    # Utilisation de Bloomz 560m (Multilingue très performant en français, taille gérable sur CPU)
    return pipeline('text-generation', model='bigscience/bloomz-560m', model_kwargs={"torch_dtype": "auto"})

generator = load_generator()

prompt = st.text_input("Donnez un début d'histoire :", "Il était une fois dans une forêt lointaine,")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Température = 0.1 (Très strict 🧊)")
    if st.button("Générer (Froid)"):
        with st.spinner("Génération..."):
            ans1 = generator(prompt, max_length=50, temperature=0.1, do_sample=True, num_return_sequences=1)
            st.info(ans1[0]['generated_text'])

with col2:
    st.subheader("Température = 1.5 (Très fou 🔥)")
    if st.button("Générer (Chaud)"):
        with st.spinner("Génération..."):
            ans2 = generator(prompt, max_length=50, temperature=1.5, do_sample=True, num_return_sequences=1)
            st.warning(ans2[0]['generated_text'])
