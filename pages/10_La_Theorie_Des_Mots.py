import streamlit as st
import graphviz

st.set_page_config(page_title="Théorie : Les Mots", page_icon="📖", layout="centered")

# 1. The Massive Hook
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>L'IA ne lit pas de mots.</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Elle ne lit que des nombres.</h3>", unsafe_allow_html=True)

st.write("")

graph = graphviz.Digraph()
graph.attr(rankdir='LR') # Left to Right layout
graph.attr('node', shape='box', style='rounded,filled', fillcolor='#f0f2f6', fontname='Helvetica', fontsize='14')

# Inputs (Words)
graph.node('A', 'Salut')
graph.node('B', 'les')
graph.node('C', 'ados')
graph.node('D', '!')

graph.node('HACHOIR', 'LE HACHOIR\n', shape='ellipse', fillcolor='#ff4b4b', fontcolor='white')

graph.node('X', '17691')
graph.node('Y', '332')
graph.node('Z', '3625')
graph.node('1', '1008')
graph.node('2', '437')
graph.node('3', '758')

# Connections
graph.edge('A', 'HACHOIR')
graph.edge('B', 'HACHOIR')
graph.edge('C', 'HACHOIR')
graph.edge('D', 'HACHOIR')

graph.edge('HACHOIR', 'X')
graph.edge('HACHOIR', 'Y')
graph.edge('HACHOIR', 'Z')
graph.edge('HACHOIR', '1')
graph.edge('HACHOIR', '2')
graph.edge('HACHOIR', '3')

# Render the graph in Streamlit
st.graphviz_chart(graph, use_container_width=True)

st.divider()

# 3. The Immediate Handoff
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Découpe tes propres phrases !", use_container_width=True):
        st.switch_page("pages/11_Les_Mots.py")