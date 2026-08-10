from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Journey P｜角色主頁", page_icon="🌿", layout="wide")
st.markdown("<style>header,#MainMenu,footer{display:none}.block-container{padding:0;max-width:none}[data-testid='stAppViewContainer']{background:#10120f}</style>", unsafe_allow_html=True)
components.html(Path(__file__).with_name("index.html").read_text(encoding="utf-8"), height=700, scrolling=False)
