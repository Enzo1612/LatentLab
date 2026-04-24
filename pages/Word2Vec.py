import streamlit as st

from gensim.models import KeyedVectors
from huggingface_hub import hf_hub_download
model = KeyedVectors.load_word2vec_format(hf_hub_download(repo_id="Word2vec/wikipedia2vec_frwiki_20180420_100d", filename="frwiki_20180420_100d.txt"))
model.most_similar("King")

# Give vector coordinates for the specified word
st.set_page_config(page_title="Calculer des mots...")

st.title("Calculs sur des mots.")

st.subheader("Donner 1 mot de départ, 1 mot à soustraire, et 1 mots à additioner.")

word1 = st.text_input("Donner le premier mot :", "Roi")
word2 = st.text_input("Donner le deuxième mot :", )