import streamlit as st
import time
import re
from datasets import load_dataset
import constants

HF_TOKEN = constants.FINE_WEB_TOKEN

DATASET_NAME = "wikimedia/wikipedia"
SUBSET = "20231101.fr"
MAX_DOCS_TO_SCAN = 10000

st.title("🔎 Wikipedia Streaming Search")

query = st.text_input("Enter search term")

start_button = st.button("Start Search")

if start_button and query:
    st.write(f"Connecting to {DATASET_NAME}...")

    try:
        pattern = re.compile(r'\b' + re.escape(query) + r'\b', re.IGNORECASE)
    except Exception as e:
        st.error(f"Invalid regex: {e}")
        st.stop()

    try:
        ds = load_dataset(
            DATASET_NAME,
            name=SUBSET,
            split="train",
            streaming=True,
            token=HF_TOKEN
        )
    except Exception as e:
        st.error(f"Connection error: {e}")
        st.stop()

    hits = 0
    scanned = 0
    start_time = time.time()

    progress_bar = st.progress(0)
    status_text = st.empty()
    results_container = st.container()

    for doc in ds:
        scanned += 1
        text = doc["text"]

        match = pattern.search(text)
        if match:
            hits += 1

            start, end = match.span()
            ctx_start = max(0, start - 50)
            ctx_end = min(len(text), end + 50)
            snippet = text[ctx_start:ctx_end].replace("\n", " ")

            # highlight match (basic HTML)
            snippet = snippet.replace(
                match.group(0),
                f"<span style='color:red;font-weight:bold'>{match.group(0)}</span>"
            )

            with results_container:
                st.markdown(f"""
                **Doc #{scanned}**  
                ...{snippet}...  
                📅 {doc.get('date', 'N/A')}
                """, unsafe_allow_html=True)

        progress_bar.progress(min(scanned / MAX_DOCS_TO_SCAN, 1.0))
        status_text.text(f"Scanned: {scanned} | Matches: {hits}")

        if scanned >= MAX_DOCS_TO_SCAN:
            break

    duration = time.time() - start_time

    st.success("Search complete")
    st.write(f"Docs: {scanned} | Matches: {hits} | Time: {duration:.2f}s")