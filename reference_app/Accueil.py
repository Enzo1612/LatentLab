import streamlit as st

st.set_page_config(page_title="Démo Séminaire IA", page_icon="🧸", layout="centered")

st.title("Séminaire IA pour les Enfants 🤖")
st.write("Bienvenue dans l'application de démonstration ! Cette application sert de référence (V1) pour comprendre le fonctionnement interne des modèles d'intelligence artificielle.")

st.markdown("""
### Explorez les concepts suivants :
1. **Word2Vec (Les mots comme des calculs)** : Comment l'IA additionne et soustrait des concepts (ex: Roi - Homme + Femme = Reine).
2. **Recherche Base de Données (Wikipédia)** : Comment l'IA cherche des informations dans de grands ensembles de données.
3. **Le Prochain Mot (Probabilités)** : Quel est le mot le plus probable pour compléter une phrase ?
4. **La Température (Créativité)** : Comment rendre l'IA plus ou moins prédictive et créative.
5. **La Limite de Mémoire (Contexte)** : Que se passe-t-il quand on donne trop d'informations à un modèle ?
""")
