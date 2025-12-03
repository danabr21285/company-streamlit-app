import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Your Advantage Group", layout="wide")

# Load your static HTML
html = Path("index.html").read_text(encoding="utf-8")

# Render it inside an iframe (JS/CSS work here)

st.components.v1.html(html, height=1100, scrolling=True)
