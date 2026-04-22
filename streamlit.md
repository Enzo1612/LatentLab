# Streamlit

## Commands

### Basics

The first command in the script. Sets browser tab title and favicon.

```python
st.set_page_config(page_title="page_title", page_icon="icon")
```

`streamlit` handles HTML and CSS. Pass it strings and it renders them.

```python
st.title("title")
st.write("text")
```

Use **radio buttons** to manage navigation. In this case streamlit creates a sidebar:

```python
st.sidebar.title("title")
st.sidebar.write("text")

page = st.sidebar.radio("Navigation", [
    "1. First page",
    "2. Second page",
    "n. Last page"
])
```

Use **switch cases** to display based on selected page.

```python
match page:
    case "1. First page":
        return
    case "2. Second page":
        return
    case "n. Last page":
        return
    case _:
        return
```

You can also create a **pages** folder. `streamlit` automatically look for it, strip the underscores and numbers to create tabs.

```bash
pages
├── 1_Le_Cerveau.py
├── 2_Les_Mots.py
└── 3_La_Mémoire.py
```

To get user input you can use an input field with a placeholder:

```python
user_input = st.user_input("Write something :", "Placeholder")
```

Create a dropdown menu using a python dictionary:

```python
selected_sentence = st.selectbox("Chose :", list(knowledge_base.keys()))
```

### Formatting

`streamlite` can render the raw integer of a token list.

```python
st.code(tokens)
```

You can use warnings to change the color of the box.

```python
st.success("String") # Green
st.info("String") # Blue
```

Create columns to rearrange the page.

```python
col1, col2 = st.columns(2)

with col1:
    st.info("Info")
    st.write(f"**{user_text}**")

with col2:
    st.success("Congrats!")
    st.write(f"**{user_text}**")
```

To make subheaders you use:

```python
st.subheader("subheader")
```

To divide the page like markdown (`---`) you use:

```python
st.divider()
```
