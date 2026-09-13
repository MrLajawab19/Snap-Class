import streamlit as st
import base64
import os

def footer_home():

    st.markdown(
        f"""
        <div style="display:flex; justify-content:center; align-items:center; flex-direction:column; margin-bottom:30px; margin-top:10px">
            <p style="text-align:center; color:#E0E3FF; font-weight:bolder;">created by <a href="https://ayushbardhani.vercel.app/">Ayush Bardhani</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

def footer_dashboard():

    st.markdown(
        f"""
        <div style="display:flex; justify-content:center; align-items:center; flex-direction:column; margin-bottom:30px; margin-top:10px">
            <p style="text-align:center; color:black; font-weight:bolder;">created by <a href="https://ayushbardhani.vercel.app/">Ayush Bardhani</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )