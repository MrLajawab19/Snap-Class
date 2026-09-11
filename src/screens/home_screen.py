import streamlit as st

from src.components.header import header_home
from src.ui.base_layout import base_layout_home, base_layout

def home_screen():
    base_layout_home()
    base_layout()
    header_home()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login as Teacher"):
            st.session_state['login_type'] = 'Teacher'
            st.rerun()

    with col2:
        if st.button("Login as Student"):
            st.session_state['login_type'] = 'Student'
            st.rerun()

