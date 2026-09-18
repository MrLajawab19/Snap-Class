import streamlit as st

from src.ui.base_layout import base_layout_dashboard, base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from src.database.db import check_teacher, create_teacher , teacher_login

def teacher_screen():
    base_layout_dashboard()
    base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == 'login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_register()


def login_teacher(teacher_username,teacher_password):
    if not teacher_username or not teacher_password:
        return False

    teacher = teacher_login(teacher_username,teacher_password)
    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.isLoggedIn = True
        return True
    return False

def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header("Welcome, " + teacher_data["name"] + "!")
    

def register_teacher(teacher_username,teacher_name,teacher_password,teacher_password_confirm):
    if not teacher_username or not teacher_name or not teacher_password or not teacher_password_confirm:
        return False, "All fields are required"
    if teacher_password != teacher_password_confirm:
        return False, "Passwords do not match"
    if check_teacher(teacher_username):
        return False, "Username already exists"

    try:
        create_teacher(teacher_username,teacher_name,teacher_password)
        return True, "Teacher registered successfully, Login now"
    except Exception as e:
        return False, f"Failed to register teacher: {str(e)}"


def teacher_screen_login():
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
        if st.button("Login",type = "primary",shortcut = 'enter',icon= ':material/passkey:', width = "stretch"):
            if login_teacher(teacher_username,teacher_password):
                st.toast("Login successful",icon = "✅")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username or password")
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

    st.divider()

    btnc1, btnc2 = st.columns(2,vertical_alignment = "center",gap = 'xxlarge')

    with btnc1:
        if st.button("Register",type = "primary",shortcut = 'enter',icon= ':material/passkey:', width = "stretch"):
            success, message = register_teacher(teacher_username,teacher_name,teacher_password,teacher_password_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)
    with btnc2:
        if st.button("Login",type = "secondary",icon = ':material/passkey:', width = "stretch"):
            st.session_state.teacher_login_type = 'login'
            st.rerun()
    
    st.space()
    footer_dashboard()

    