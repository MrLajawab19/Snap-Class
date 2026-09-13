import streamlit as st
import base64
import os

def header_home():
    img_path = os.path.join(os.path.dirname(__file__), '..', '..', 'public', 'SnapClass Logo.png')
    with open(img_path, 'rb') as f:
        img_b64 = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <div style = "display : flex; justify-content : center ; align-items : center; flex-direction : column; margin-bottom : 30px; margin-top : 10px">
            <img src='data:image/png;base64,{img_b64}' width='250' height='250'>
            <h1 style = "text-align : center; color : #E0E3FF;">SNAP<br/>CLASS</h1>
        </div>
        """,
        unsafe_allow_html=True
    )