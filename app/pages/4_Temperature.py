import streamlit as st
from transformers import pipeline

# Ajout d'onglets pour séparer la théorie (la "slide") de la pratique (la "démo")
tab_theorie, tab_demo = st.tabs(["📖 Théorie : La Température", "⚙️ Expérience Interactive"])

with tab_theorie:
    st.title("La Température de l'IA")
    
    # On simule l'apparence d'une vraie slide de présentation
    st.markdown("""
    <div style='background-color: #141B2D; padding: 30px; border-radius: 15px; border: 1px solid #00E5FF; text-align: center;'>
        <h2 style='color: #00E5FF;'>Régler le curseur de l'imagination</h2>
        <p style='font-size: 20px; line-height: 1.6;'>
            Le cerveau de l'IA ne génère pas de mots, il génère des <strong>probabilités</strong>.<br><br>
            La <strong>Température</strong> est un procédé mathématique qui aplatit ou aiguise ces probabilités :<br>
        </p>
        <div style='display: flex; justify-content: space-around; margin-top: 30px;'>
            <div style='background-color: rgba(0, 229, 255, 0.1); padding: 20px; border-radius: 10px; width: 45%;'>
                <h3>❄️ Froid</h3>
                <p>L'IA choisit <strong>strictement</strong> le mot le plus probable.<br>Résultat : Logique, formel, prévisible.</p>
            </div>
            <div style='background-color: rgba(255, 100, 100, 0.1); padding: 20px; border-radius: 10px; width: 45%;'>
                <h3>🔥 Chaud</h3>
                <p>Les mots rares ont soudainement leur chance d'être choisis !<br>Résultat : Créativité, folie, hallucination.</p>
            </div>
        </div>
    </div>
    <br>
    <p style='text-align: center; color: gray;'><em>(Passez à l'onglet Expérience Interactive en haut 👆 pour lancer l'action)</em></p>
    """, unsafe_allow_html=True)
    
    # Optionnel : Insérer un GIF ou un graphique Lottie animée ici plus tard :
    # st.image("https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif", use_column_width=True)

with tab_demo:
    st.title("Le Module de Température !")
    st.write("Si la température est à 0, l'IA est mathématique et logique. Si elle monte, l'IA devient créative... ou folle !")

    @st.cache_resource
    def load_generator():
        # Modele francais de 1.3 milliard de param
        return pipeline('text-generation', model='croissantllm/CroissantLLMBase')

    generator = load_generator()

    prompt = st.text_input("Donnez un début d'histoire :", "Il était une fois, dans une forêt magique et lointaine,")

    tokens_to_generate = 150

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("Température : 0.2")
            if st.button("Générer", key="btn_temp_low", use_container_width=True):
                with st.spinner("Génération..."):
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
        with st.container(border=True):
            st.subheader("Température : 1.6")
            if st.button("Générer", key="btn_temp_high", use_container_width=True):
                with st.spinner("Génération..."):
                    ans2 = generator(
                        prompt, 
                        max_new_tokens=tokens_to_generate, 
                        temperature=1.6, 
                        do_sample=True, 
                        repetition_penalty=1.2,
                        num_return_sequences=1
                    )
                    st.warning(ans2[0]['generated_text'])
