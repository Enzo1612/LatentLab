import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_qa_model():
    return pipeline('question-answering', model='etalab-ia/camembert-base-squadFR-fquad-piaf')

qa_engine = load_qa_model()

tab_theorie, tab_demo = st.tabs(["📖 Théorie : La Mémoire Courte", "⚙️ Expérience Interactive"])

with tab_theorie:
    st.title("La Fenêtre de Contexte")
    
    st.markdown("""
    <div style='background-color: #141B2D; padding: 30px; border-radius: 15px; border: 1px solid #00E5FF; text-align: center;'>
        <h2 style='color: #00E5FF;'>La Baignoire de l'Oubli</h2>
        <p style='font-size: 20px; line-height: 1.6;'>
            L'IA n'a pas une mémoire infinie. Il faut imaginer <strong>sa mémoire de travail</strong> comme une boîte qui retient un nombre précis de mots.<br><br>
        </p>
        <div style='display: flex; justify-content: space-around; margin-top: 30px;'>
            <div style='background-color: rgba(0, 229, 255, 0.1); padding: 20px; border-radius: 10px; width: 45%;'>
                <h3>📥 L'Ajout de texte</h3>
                <p>À chaque nouveau message, le texte entre dans la mémoire mathématique de l'IA.</p>
            </div>
            <div style='background-color: rgba(255, 100, 100, 0.1); padding: 20px; border-radius: 10px; width: 45%;'>
                <h3>🗑️ Le Débordement</h3>
                <p>Quand la boîte est pleine, les mots les plus anciens <strong>débordent et s'effacent</strong> pour faire de la place aux mots récents !</p>
            </div>
        </div>
    </div>
    <br>
    <p style='text-align: center; color: gray;'><em>(Passez à l'onglet Expérience Interactive en haut 👆 pour la démo)</em></p>
    """, unsafe_allow_html=True)

with tab_demo:
    st.title("5. Les Limites de la Mémoire")
    st.write("Si on donne trop d'informations d'un coup à une IA, elle oublie son passé !")

    fact = st.text_input("Donnez-moi un fait à retenir :", "Le grand mot de passe caché du coffre fort est: SAPIN_ROI.")
    question = st.text_input("Posez-moi une question sur ce fait :", "Quel est le grand mot de passe caché du coffre fort ?")

    st.markdown("---")
    words_count = st.slider("Combien de mots inutiles insérer dans la conversation ?", 0, 800, 50)

    if st.button("Tester la mémoire de l'IA"):
        with st.spinner("L'IA lit le texte et cherche la réponse..."):

            filler_words = ["pomme", "oiseau", "arbre", "voiture", "maison", "soleil", "route", "chat", "chien", "livre", "bureau", "mer", "montagne", "herbe", "fleur"]
            filler_list = [filler_words[i % len(filler_words)] for i in range(words_count)]
            filler = " ".join(filler_list)

            full_context = f"Fait initial: {fact}\n... {filler} ..."

            st.write("### Le contexte reçu par l'IA :")
            st.info(f"L'IA doit analyser un document de **{len(full_context.split())} mots** au total.")
            
            with st.expander("Voir le contenu exact de sa mémoire"):
                st.text(full_context)
                    
            st.markdown("---")

            try:
                fenetre_max = 200
                mots = full_context.split()
                if len(mots) > fenetre_max:
                    contexte_tronque = " ".join(mots[-fenetre_max:])
                    st.warning(f"⚠️ Alerte mémoire pleine ! L'IA ne peut retenir que {fenetre_max} mots. Les {len(mots)-fenetre_max} plus vieux s'effacent de sa mémoire instantanément !")
                else:
                    contexte_tronque = full_context
                    
                answer = qa_engine(
                    question=question,
                    context=contexte_tronque
                )

                if isinstance(answer, list):
                    answer = answer[0]

                result = answer["answer"]
                score = answer["score"]
                
                st.write("### La réponse finale trouvée :")
                
                if score < 0.1:
                    st.error(f"**J'ai trouvé : '{result}'** (Sûr à seulement {score*100:.1f}%)")
                    st.error("Elle ne sait pas... Le tout premier fait a été effacé de la machine !")
                else:
                    st.success(f"**J'ai trouvé : '{result}'** (Confiance à {score*100:.1f}%)")
                    st.success("Bravo ! L'histoire était assez courte pour ne pas faire déborder sa mémoire.")

            except Exception as e:
                st.error("L'IA n'a **RIEN** trouvé !")
                st.error(f"Erreur technique : {e}")
