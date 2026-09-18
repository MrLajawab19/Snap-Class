import streamlit as st

from src.ui.base_layout import base_layout_dashboard, base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from PIL import Image

import numpy as np

def student_screen():
    base_layout_dashboard()
    base_layout()

    c1, c2 = st.columns(2,vertical_alignment = "center",gap = 'xxlarge')

    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back Home",type = "secondary",key="loginbackbtn",shortcut = 'control+backspace'):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login Using Your Face ID", text_alignment="center")
    st.space()
    st.space()
    photo_source = st.camera_input("Position your face in the center of the frame")

    if photo_source:
        np.array(Image.open(photo_source))
        
    footer_dashboard()





