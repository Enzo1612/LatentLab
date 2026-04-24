import streamlit as st
from transformers import pipeline

st.title("4. La Température (La Créativité) 🌡️")
st.write("Si la température est à 0, l'IA est mathématique et logique. Si elle monte, l'IA devient créative... ou folle !")

@st.cache_resource
def load_generator():
    # CroissantLLM est un modèle français de 1.3 Milliard de paramètres,
    # spécifiquement entraîné sur des données francophones de haute qualité (par CentraleSupélec et Illuin)
    # Idéal pour raconter de vraies histoires en français sans dévier vers l'anglais !
    return pipeline('text-generation', model='croissantllm/CroissantLLMBase')

generator = load_generator()

prompt = st.text_input("Donnez un début d'histoire :", "Il était une fois, dans une forêt magique et lointaine,")

# Quelques réglages pour de belles histoires
# max_new_tokens (au lieu de max_length global) garantit la taille de l'ajout
# repetition_penalty empêche l'IA de bégayer, surtout à basse température.
tokens_to_generate = 150

col1, col2 = st.columns(2)

with col1:
    st.subheader("Température = 0.2 (Très strict 🧊)")
    if st.button("Générer (Froid)"):
        with st.spinner("Génération (env. 30 sec)..."):
            ans1 = generator(
                prompt, 
                max_new_tokens=tokens_to_generate, 
                temperature=0.2, 
                do_sample=True, 
                repetition_penalty=1.2,
                num_return_sequences=1
            )
            st.info(ans1[0]['generated_text'])

with col2:
    st.subheader("Température = 1.6 (Très créatif 🔥)")
    if st.button("Générer (Chaud)"):
        with st.spinner("Génération (env. 30 sec)..."):
            ans2 = generator(
                prompt, 
                max_new_tokens=tokens_to_generate, 
                temperature=1.6, 
                do_sample=True, 
                repetition_penalty=1.2,
                num_return_sequences=1
            )
            st.warning(ans2[0]['generated_text'])
