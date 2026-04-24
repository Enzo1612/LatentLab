import streamlit as st
from transformers import pipeline

st.title("5. Les Limites de la Mémoire 🧠")
st.write("L'IA n'a pas une mémoire infinie. Si on lui donne trop d'informations d'un coup, elle oublie le début de la conversation !")

@st.cache_resource
def load_generator():
    return pipeline('text-generation', model='bigscience/bloomz-560m', model_kwargs={"torch_dtype": "auto"})

generator = load_generator()

fact = st.text_input("Donnez-moi un fait à retenir :", "Le grand mot de passe caché du coffre fort est: SAPIN_ROI.")
question = st.text_input("Posez-moi une question sur ce fait :", "Quel est le mot de passe du coffre ?")

words_count = st.slider("Combien de texte inutile insérer entre le fait et la question ?", 10, 2000, 50)

if st.button("Tester la mémoire..."):
    with st.spinner("Je lis tout ce texte..."):
        # Texte inutile pour remplir le contexte
        filler = "bla " * words_count
        
        # Contexte complet
        full_context = f"Fait initial: {fact}. {filler} \nQuestion: {question}\nRéponse:"
        
        # Le modèle a une limite de contexte (habituellement 1024 pour gpt2/petit modele)
        try:
            answer = generator(full_context, max_new_tokens=20, do_sample=False)
            generated = answer[0]['generated_text']
            
            # Ne garder que ce que l'IA a produit après le prompt
            result = generated[len(full_context):]
            
            st.write("### La réponse de l'IA :")
            st.code(result.strip() or "(Pas de réponse compréhensible)")
            
            if words_count > 500:
                st.error("L'IA a probablement dit n'importe quoi car son 'contexte' était rempli par les 'bla bla'. Elle a complètement oublié le début !")
            else:
                st.success("Tant que le texte est court, l'IA s'en souvient !")
        except Exception as e:
            st.error(f"L'IA a explosé à cause d'une limite technique ! (Erreur : {e})")
