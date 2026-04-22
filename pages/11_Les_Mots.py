import streamlit as st
import tiktoken

st.set_page_config(page_title="Tokens & Embeddings", page_icon="🧩")

st.title("Étape 1 : Le Découpage ✂️")
st.markdown("> **L'IA ne lit pas les lettres. Elle lit des nombres.**") 

encoder = tiktoken.get_encoding("cl100k_base")

# Larger text input
user_text = st.text_input("Écris une phrase pour la machine :", "Salut les ados !")

if user_text:
    tokens = encoder.encode(user_text)
    
    st.write("") # Spacer
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("👤 Ce que tu as écrit :")
        st.subheader(f"*{user_text}*")
        
    with col2:
        st.error("🤖 Ce que l'IA comprend :")
        # Display as a clean list of numbers, not a raw python array
        token_string = " • ".join([str(t) for t in tokens])
        st.subheader(token_string)
        
    st.divider()
    st.metric(label="Nombre de blocs (Tokens) générés", value=len(tokens))