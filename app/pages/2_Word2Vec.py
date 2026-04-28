import os
import streamlit as st
# Remplacer KeyedVectors par load_facebook_vectors
from gensim.models.fasttext import load_facebook_vectors

@st.cache_resource
def load_model():
    script_dir = os.path.dirname(__file__) 
    chemin_modele = os.path.join(script_dir, "..", "..", "models", "cc.fr.300.bin")
    chemin_modele = os.path.abspath(chemin_modele)
    
    # Utiliser le loader Facebook pour les fichiers FastText
    return load_facebook_vectors(chemin_modele)

model = load_model()

tab_theorie, tab_demo = st.tabs(["📖 Théorie : Les Mots en Nombres", "⚙️ Expérience Interactive"])

with tab_theorie:
    st.title("Comment l'IA comprend-elle les mots ?")
    
    st.markdown("""
    <div style='background-color: #141B2D; padding: 30px; border-radius: 15px; border: 1px solid #00E5FF; text-align: center;'>
        <h2 style='color: #00E5FF;'>Les Mots sont des Coordonnées GPS</h2>
        <p style='font-size: 20px; line-height: 1.6;'>
            Un ordinateur ne comprend pas les lettres. Pour donner du sens aux mots, l'IA les transforme en longues suites de nombres qu'on appelle des <strong>Vecteurs</strong>.<br><br>
        </p>
        <div style='display: flex; justify-content: space-around; margin-top: 30px;'>
            <div style='background-color: rgba(0, 229, 255, 0.1); padding: 20px; border-radius: 10px; width: 45%;'>
                <h3>🗺️ L'Espace Sémantique</h3>
                <p>Les mots qui parlent de la même chose (Chien, Chat, Animal) ont des coordonnées proches. L'IA sait qu'ils sont voisins dans son "Espace Vectoriel" !</p>
            </div>
            <div style='background-color: rgba(255, 100, 100, 0.1); padding: 20px; border-radius: 10px; width: 45%;'>
                <h3>🧮 L'Algèbre des Idées</h3>
                <p>Puisque ce sont des nombres, on peut faire des mathématiques avec des idées : les additionner et les soustraire pour créer de nouveaux concepts !</p>
            </div>
        </div>
    </div>
    <br>
    <p style='text-align: center; color: gray;'><em>(Passez à l'onglet Expérience Interactive en haut 👆 pour faire des maths avec l'IA)</em></p>
    """, unsafe_allow_html=True)

with tab_demo:
    st.title("1. Word2Vec : Calculer avec des Mots")
    st.write("Vérifions si la machine a vraiment compris les concepts ! Faisons des mathématiques avec le sens des mots.")

    st.subheader("Additionner et Soustraire le sens")
    col1, col2, col3, col4 = st.columns([2, 1, 2, 1])
    with col1:
        word1 = st.text_input("Mot 1", "roi").lower()
    with col2:
        st.write("➖")
    with col3:
        word2 = st.text_input("Mot 2", "homme").lower()

    word3 = st.text_input("➕ Mot 3", "femme").lower()

    if st.button("Calculer le résultat 🟰"):
        try:
            # Résultat: Mot1 - Mot2 + Mot3
            raw_results = model.most_similar(positive=[word1, word3], negative=[word2], topn=30)
            
            # Filtrer pour empêcher les mots d'origine ou leurs variations évidentes d'apparaître
            input_words = {word1, word2, word3}
            filtered_results = []
            seen_words = set()
            
            for word, score in raw_results:
                word_lower = word.lower()
                
                # Ignorer les mots avec des caractères spéciaux, ponctuation ou chiffres
                if not word_lower.replace("-", "").isalpha():
                    continue
                    
                # Ignorer les doublons (ex: "Reine" et "reine")
                if word_lower in seen_words:
                    continue
                    
                # On vérifie que le mot n'est pas l'un de nos mots d'entrée
                # ni une variation très basique (par exemple inclut l'entrée, ou l'entrée l'inclut)
                is_input = any(word_lower == w or word_lower == w + "s" or word_lower == w + "x" for w in input_words)
                if not is_input:
                    filtered_results.append((word, score))
                    seen_words.add(word_lower)
                
                # On s'arrête quand on a nos 3 résultats propres
                if len(filtered_results) == 3:
                    break
                    
            st.success("Voici les mots les plus proches du résultat :")
            if filtered_results:
                for word, score in filtered_results:
                    st.write(f"- **{word}** (confiance: {score:.2f})")
            else:
                st.warning("Je n'ai pas trouvé de corrélation forte en dehors des mots tapés.")
                
        except KeyError as e:
            st.error(f"Désolé, je ne connais pas ce mot : {e}. Essayez des mots simples pour cette démo.")
