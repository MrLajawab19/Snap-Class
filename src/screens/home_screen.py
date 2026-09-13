from starlette import applications
import streamlit as st

from src.components.header import header_home
from src.ui.base_layout import base_layout_home, base_layout
from src.components.footer import footer_home

def home_screen():
    base_layout_home()
    base_layout()
    header_home()

    col1, col2 = st.columns(2,gap = 'large')
    with col1:
        st.header("I'm Teacher")
        st.image("public\Teacher.png",width=100)
        if st.button("Login as Teacher",type = "primary", icon = ':material/arrow_outward:', icon_position= 'right'):
            st.session_state['login_type'] = 'Teacher'
            st.rerun()

    with col2:
        st.header("I'm Student")
        st.image("public\Student.png",width=100)
        if st.button("Login as Student",type = "primary", icon = ':material/arrow_outward:', icon_position= 'right'):
            st.session_state['login_type'] = 'Student'
            st.rerun()

    footer_home()
