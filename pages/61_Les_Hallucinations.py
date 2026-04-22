import streamlit as st

st.set_page_config(page_title="Les Hallucinations", page_icon="👻")

st.title("Étape 6 : Les Hallucinations 👻")
st.markdown("> **L'IA ne sait pas ce qui est vrai ou faux. Elle sait juste ce qui est probable.**")

# Clean, segmented control instead of a basic radio button
trap_type = st.segmented_control(
    "Choisis un piège :",
    ["Histoire", "Mathématiques", "Logique des Mots"],
    default="Histoire"
)

st.divider()

if trap_type == "Histoire":
    st.info("**Prompt :** Raconte-moi l'exploration de la planète Mars par Christophe Colomb en 1492.")
    st.error("**L'IA répond avec une confiance absolue :**\n\n> En 1492, après avoir traversé l'océan cosmique avec ses vaisseaux, Christophe Colomb a posé le pied sur le sol rouge de Mars...")
    
    # Suspense mechanism: hides the answer until you click it
    with st.expander("🔍 Pourquoi a-t-elle menti ? (Clique pour voir le secret)"):
        st.write("Le prompt associe 'Christophe Colomb' et '1492' à 'Exploration'. L'IA calcule que le mot 'vaisseau' ou 'découverte' est probable, même si historiquement, c'est absurde. Elle veut juste finir ta phrase de manière statistique.")

elif trap_type == "Mathématiques":
    st.info("**Prompt :** Qu'est-ce qui est le plus lourd : un kilo de plumes ou un kilo et demi de plomb ?")
    st.error("**L'IA répond avec une confiance absolue :**\n\n> Un kilo de plomb est plus lourd qu'un kilo de plumes car le plomb a une densité plus élevée.")
    
    with st.expander("🔍 Pourquoi a-t-elle menti ?"):
        st.write("Elle a lu 'plumes', 'plomb' et 'lourd'. Elle a recraché la statistique de la blague classique, en oubliant de lire le 'un kilo et demi'. Elle ne calcule pas, elle prédit.")

elif trap_type == "Logique des Mots":
    st.info("**Prompt :** Combien y a-t-il de lettres 'r' dans le mot 'fraise' ?")
    st.error("**L'IA répond avec une confiance absolue :**\n\n> Il y a deux lettres 'r' dans le mot fraise.")
    
    with st.expander("🔍 Pourquoi a-t-elle menti ?"):
        st.write("**Rappelle-toi de l'Étape 1 (Les Tokens) !** L'IA ne voit pas F-R-A-I-S-E. Elle voit le nombre '8493'. Elle est physiquement incapable de compter des lettres à l'intérieur d'un nombre.")