import streamlit as st
from transformers import pipeline

st.title("5. Les Limites de la Mémoire")
st.write("L'IA n'a pas une mémoire infinie. Si on lui donne trop d'informations d'un coup, elle oublie le début de la conversation !")

@st.cache_resource
def load_qa_model():
    # Pipeline "question-answering" (type RAG)
    # L'IA est obligée d'extraire la réponse du texte, elle ne peut rien inventer.
    # Etalab CamemBERT est LA référence française pour ça.
    return pipeline('question-answering', model='etalab-ia/camembert-base-squadFR-fquad-piaf')

qa_engine = load_qa_model()

fact = st.text_input("Donnez-moi un fait à retenir :", "Le grand mot de passe caché du coffre fort est: SAPIN_ROI.")
question = st.text_input("Posez-moi une question sur ce fait :", "Quel est le grand mot de passe caché du coffre fort ?")

st.markdown("---")
words_count = st.slider("Combien de texte inutile insérer entre le fait et la question ?", 0, 3000, 50)

if st.button("Tester la mémoire de l'IA"):
    with st.spinner("L'IA lit le texte et réfléchit..."):
        # Texte inutile pour remplir le contexte (Créons des phrases bidons plutôt qu'une répétition infinie d'une syllabe qui casse les modèles)
        # Répéter des milliers de fois "bla" active le mécanisme d'hallucination d'un LLM, on veut juste remplir son contexte proprement.
        filler_phrase = "Il fait très beau aujourd'hui. Les oiseaux chantent dans les arbres. Je suis allé manger une pomme. "
        filler = filler_phrase * (words_count // 10)
        
        # Format du document "Recherche/RAG"
        # On met le mot de passe DANS LE TEXTE, et l'IA doit le chercher
        full_context = f"Fait initial: {fact}\n... {filler} ..."

        st.write("### Le contexte de l'IA (Le document qu'elle lit) :")
        st.info(f"L'IA a reçu un document de **{len(full_context.split())} mots**.")
        
        with st.expander("Afficher le texte donné à l'IA"):
            if len(full_context) > 5000:
                short_display = full_context[:1000] + "\n\n[... MILLIERS DE MOTS INUTILES ...]\n\n" + full_context[-500:]
                st.text(short_display)
            else:
                st.text(full_context)
                
        st.markdown("---")
        
        # Limite contexte de CamemBERT = 512 tokens
        try:
            # On donne la question et le texte (Contexte). L'IA ne peut faire que de l'extraction.
            # max_seq_len bloque la taille de la recherche comme un vrai modèle technique !
            answer = qa_engine(question=question, context=full_context, max_seq_len=512)
            result = answer['answer']
            score = answer['score']
            
            st.write("### La réponse de l'IA :")
            st.success(f"**J'ai trouvé : '{result}'** (Confiance à {score*100:.1f}%)")
            
            if words_count > 500:
                st.warning("Miracle, l'IA a réussi à trouver l'information au milieu de ce tas de texte !")
            else:
                st.success("C'est facile, le texte est très court !")
                
        except Exception as e:
            st.write("### La réponse de l'IA :")
            st.error("L'IA n'a **RIEN** trouvé !")
            st.error("Raison : Le document était trop long par rapport à sa limite de contexte (512 jetons max !). L'information a été écrasée par les phrases inutiles.")
            st.error("Raison : Le texte était trop long pour sa fenêtre de contexte mathématique. Le début de la phrase a été écrasé, ou la mémoire RAM est pleine.")
