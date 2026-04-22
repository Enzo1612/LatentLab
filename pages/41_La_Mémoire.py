import streamlit as st

st.set_page_config(page_title="La Mémoire", page_icon="📚")

st.title("Étape 4 : La Fenêtre de Contexte")
st.markdown("> **Quand l'IA lit trop de texte, elle n'explose pas... elle oublie le début.**")

CONTEXT_LIMIT = 40 

st.write(f"Imaginons une IA avec une mémoire minuscule : **{CONTEXT_LIMIT} mots maximum**.")

secret_word = st.text_input("1. Cache un mot important au début :", "Licorne")
noise_level = st.slider("2. Ajoute du texte inutile (bla bla bla) :", 0, 100, 10)


document = [f"**{secret_word}**"] + ["bla"] * noise_level

total_words = len(document)

if total_words > CONTEXT_LIMIT:
    overflow_count = total_words - CONTEXT_LIMIT
    forgotten_words = document[:overflow_count]
    remembered_words = document[overflow_count:]
else:
    forgotten_words = []
    remembered_words = document

st.divider()
st.subheader("Le Cerveau de l'IA en temps réel :")

col1, col2 = st.columns(2)

# Column 1: The Active Memory (Green)
with col1:
    st.success(f"🟢 Mémoire Active ({len(remembered_words)}/{CONTEXT_LIMIT} mots)")
    st.write(" ".join(remembered_words))

# Column 2: The Forgotten Zone (Red/Grey)
with col2:
    st.error(f"🔴 Zone d'Oubli ({len(forgotten_words)} mots supprimés)")
    if forgotten_words:
        # We use strikethrough (~~) to visually show deletion
        strikethrough_text = " ".join([f"~~{w}~~" for w in forgotten_words])
        st.markdown(f"<span style='color:grey'>{strikethrough_text}</span>", unsafe_allow_html=True)
    else:
        st.write("*Rien n'a été oublié pour l'instant.*")