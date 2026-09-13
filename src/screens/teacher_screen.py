import streamlit as st

from src.ui.base_layout import base_layout_dashboard, base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

def teacher_screen():
    base_layout_dashboard()
    base_layout()

    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == 'login':
        teacher_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_register()


def teacher_login():
    c1, c2 = st.columns(2,vertical_alignment = "center",gap = 'xxlarge')

    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back Home",type = "secondary",key="loginbackbtn",shortcut = 'control+backspace'):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login Using Password", text_alignment="center")
    st.space()
    st.space()
    teacher_username = st.text_input("Your Username",key = "teacher_username", placeholder = "Ayush")
    teacher_password = st.text_input("Your Password",key = "teacher_password", placeholder = "Password",type = "password")

    st.divider()

    btnc1, btnc2 = st.columns(2,vertical_alignment = "center",gap = 'xxlarge')

    with btnc1:
        st.button("Login",type = "primary",shortcut = 'enter',icon= ':material/passkey:', width = "stretch")
    with btnc2:
        if st.button("Register Yourself",type = "secondary",icon = ':material/passkey:', width = "stretch"):
            st.session_state.teacher_login_type = 'register'
            st.rerun()
    
    st.space()
    footer_dashboard()

def teacher_register():
    c1, c2 = st.columns(2,vertical_alignment = "center",gap = 'xxlarge')

    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back Home",type = "secondary",key="backbtn",shortcut = 'control+backspace'):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Register Your Teacher Profile", text_alignment="center")
    st.space()
    st.space()
    teacher_username = st.text_input("Your Username",key = "teacher_username", placeholder = "@Ayush")
    teacher_name = st.text_input("Your Full name",key = "teacher_name", placeholder = "Ayush Bardhani")
    teacher_password = st.text_input("Your Password",key = "teacher_password", placeholder = "Password",type = "password")
    teacher_password_confirm = st.text_input("Confirm Your Password",key = "teacher_password_confirm", placeholder = "Password",type = "password")
    teacher_gender = st.selectbox("Gender",key = "teacher_gender", options = ["Male","Female","Other"])

    st.divider()

    btnc1, btnc2 = st.columns(2,vertical_alignment = "center",gap = 'xxlarge')

    with btnc1:
        st.button("Register",type = "primary",shortcut = 'enter',icon= ':material/passkey:', width = "stretch")
    with btnc2:
        if st.button("Login",type = "secondary",icon = ':material/passkey:', width = "stretch"):
            st.session_state.teacher_login_type = 'login'
            st.rerun()
    
    st.space()
    footer_dashboard()

    