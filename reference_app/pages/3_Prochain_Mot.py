import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import matplotlib.pyplot as plt

st.title("3. Devancer le Prochain Mot 🔮")
st.write("Les IA comme ChatGPT ne font que prédire le *prochain mot* ! Voyons comment.")

@st.cache_resource
def load_hf_model():
    # Bloomz-560m est un modèle multilingue (français très fort car créé par le CNRS/BigScience) 
    # de petite taille (560M de paramètres)
    model_name = "bigscience/bloomz-560m" 
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_hf_model()

# Une phrase tournée spécifiquement pour appeler un nom propre (pays/concept)
sentence = st.text_input("Commencez une phrase :", "L'explorateur Christophe Colomb est célèbre pour avoir découvert")

if st.button("Voir les probabilités du prochain mot"):
    with st.spinner("Calcul des probabilités..."):
        inputs = tokenizer(sentence, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
        
        next_token_logits = outputs.logits[0, -1, :]
        next_token_probs = torch.nn.functional.softmax(next_token_logits, dim=-1)
        
        # On récupère les 100 meilleurs pour pouvoir filtrer les mots de liaison "inutiles" 
        top_k_large = 100
        top_probs, top_indices = torch.topk(next_token_probs, top_k_large)
        
        # Liste de "stop words" français (et anglais) très complète pour ne garder que le "sens"
        stop_words = {
            "le", "la", "les", "l", "un", "une", "des", "d", "de", "du", "à", "au", "aux", 
            "ce", "cet", "cette", "ces", "mon", "ton", "son", "ma", "ta", "sa", "mes", "tes", "ses",
            "et", "en", "ou", "où", "par", "pour", "dans", "sur", "avec", "sans", "sous", "vers",
            "qui", "que", "qu", "quoi", "dont", 
            "il", "elle", "on", "nous", "vous", "ils", "elles", "je", "tu", "y",
            "est", "sont", "a", "ont", "être", "avoir", "été",
            "ne", "pas", "plus", "jamais",
            "the", "a", "an", "that", "this", "to", "of", "and", "in"
        }
        
        filtered_labels = []
        filtered_values = []
        
        for prob, idx in zip(top_probs, top_indices):
            word_raw = tokenizer.decode([idx.item()])
            word = word_raw.strip()
            word_lower = word.lower()
            
            # Nettoyage pour ignorer les apostrophes isolées comme l' ou qu'
            word_clean = word_lower.replace("'", "")
            
            # On ignore les mots trop courts, la ponctuation, et les mots de liaison évidents
            if len(word_clean) > 1 and word_clean.isalpha() and word_clean not in stop_words:
                filtered_labels.append(word)
                filtered_values.append(prob.item())
            
            if len(filtered_labels) == 5:
                break
                
        # Si après filtrage on n'a rien (très rare), on retombe sur le top 5 brut
        if len(filtered_labels) == 0:
            filtered_labels = [tokenizer.decode([idx.item()]).strip() for idx in top_indices[:5]]
            filtered_values = top_probs[:5].tolist()
        
        # Recalculer les probabilitées relatives entre ces 5 mots (pour que la barre la plus haute touche le haut si on le souhaite)
        # Mais pour être honnête sur l'IA, on affiche la VRAIE probabilité mathématique
        
        st.write("Voici les mots importants auxquels je pense pour la suite :")
        
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(filtered_labels, [v * 100 for v in filtered_values], color='coral')
        ax.set_ylabel('Probabilité Brute (%)')
        st.pyplot(fig)
