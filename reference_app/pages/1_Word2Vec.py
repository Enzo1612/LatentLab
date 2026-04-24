import os
import streamlit as st
# Remplacer KeyedVectors par load_facebook_vectors
from gensim.models.fasttext import load_facebook_vectors

st.title("1. Additionner les mots?")
st.write("Comment l'IA comprend-elle les liens entre les mots ? En les transformant en nombres !")

@st.cache_resource
def load_model():
    script_dir = os.path.dirname(__file__) 
    chemin_modele = os.path.join(script_dir, "..", "..", "models", "cc.fr.300.bin")
    chemin_modele = os.path.abspath(chemin_modele)
    
    # Utiliser le chargeur Facebook pour les fichiers FastText
    return load_facebook_vectors(chemin_modele)

model = load_model()


st.subheader("Faisons des mathématiques avec des mots !")
col1, col2, col3, col4 = st.columns([2, 1, 2, 1])
with col1:
    word1 = st.text_input("Mot 1", "king").lower()
with col2:
    st.write("➖")
with col3:
    word2 = st.text_input("Mot 2", "man").lower()

word3 = st.text_input("➕ Mot 3", "woman").lower()

if st.button("Calculer le résultat 🟰"):
    try:
        # Résultat: Mot1 - Mot2 + Mot3
        # On demande plus de résultats (topn=30) car on va filtrer fortement
        raw_results = model.most_similar(positive=[word1, word3], negative=[word2], topn=30)
        
        # Filtrer pour empêcher les mots d'origine ou leurs variations évidentes d'apparaître
        input_words = {word1, word2, word3}
        filtered_results = []
        seen_words = set()
        
        for word, score in raw_results:
            word_lower = word.lower()
            
            # Ignorer les mots avec des caractères spéciaux, ponctuation ou chiffres (on garde les lettres et tirets)
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
