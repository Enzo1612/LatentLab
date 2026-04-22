import streamlit as st

st.set_page_config(page_title="La Température", page_icon="🌡️")

st.title("Étape 3 : La Température")
st.markdown("> **Comment l'IA passe d'un robot prévisible à un artiste fou.**")

st.write("La 'Température' est un réglage qui contrôle la **créativité** du modèle.")

# 1. The Context
st.info("Prompt donné à l'IA : **'La nuit dernière, j'ai vu...'**")

# 2. The Interactive Slider
# Ranges from 0.0 to 2.0. Default is 0.7 (standard LLM temperature).
temp = st.slider("Règle le curseur de Température :", 0.0, 1.0, 0.2, step=0.2)

st.divider()

# 3. The Generative States
# We hardcode the outcomes to guarantee an instant, risk-free live presentation.
if temp < 0.25:
    st.subheader("Mode Robot")
    st.write("*L'IA choisit systématiquement le mot avec la plus haute probabilité.*")
    st.success("La nuit dernière, j'ai vu un chat. Le chat était noir. J'aime les chats.")

elif temp < 0.5:
    st.subheader("Mode Équilibré")
    st.write("*L'IA mélange logique et un peu de hasard pour paraître naturelle.*")
    st.success("La nuit dernière, j'ai vu une étoile filante traverser le ciel dégagé.")

elif temp <= 0.75:
    st.subheader("Mode Artiste")
    st.write("*L'IA prend de gros risques et choisit des mots très improbables.*")
    st.success("La nuit dernière, j'ai vu des rivières de néon murmurer des secrets aux hiboux d'argent.")

else:
    st.subheader("Mode Chaos")
    st.write("*Le système s'effondre. La probabilité n'a plus de sens.*")
    st.success("La nuit dernière, j'ai vu clignotant girafe tourner vite plafond pourquoi bleu !")