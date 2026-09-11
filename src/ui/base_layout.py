import streamlit as st

def base_layout_home():

    st.markdown(
        """
        <style>
            .stApp {
                background-color : #5865f2 !important;
            }


        </style>

        """,
            unsafe_allow_html=True)

def base_layout_dashboard():

    st.markdown(
        """
        <style>
            .stApp {
                background-color : #E0E3FF !important;
            }


        </style>

        """,
            unsafe_allow_html=True)

def base_layout():

    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Caacupe+One&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Caacupe+One&family=Outfit:wght@100..900&display=swap');



            #MainMenu,footer,header{
                visibility : hidden;
            }

            .block-container{
                padding-top : 1.5rem !important}

            h1 {
                font-family : "Caacupe One" !important;
                font-size : 3.5rem !important;
                line-height : 0.9 !important;
                margin-bottom : 0rem !important;
                color : white !important;
            }

            h2 {
                font-family : "Caacupe One" !important;
                font-size : 3.5rem !important;
                line-height : 0.9 !important;
                margin-bottom : 0rem !important;
                color : white !important;
            }

            h3, h4, p {
                font-family : "Outfit" !important;
            }

            button{
                border-radius : 1.5rem !important;
                background : #5865F2 !important;
                color :white !important;
                padding : 10px 20px !important;
                border : none !important;
                transition : transform 0.25s ease-in-out !important;
            }


            button[kind = "secondary"]{
                border-radius : 1.5rem !important;
                background : #EB459E !important;
                color :white !important;
                padding : 10px 20px !important;
                border : none !important;
                transition : transform 0.25s ease-in-out !important;
            }

            button[kind = "tertiary"]{
                border-radius : 1.5rem !important;
                background : black !important;
                color :white !important;
                padding : 10px 20px !important;
                border : none !important;
                transition : transform 0.25s ease-in-out !important;
            }

            button:hover{
                transform : scale(1.05);
            }

            button[kind = "secondary"]:hover{
                transform : scale(1.05);
            }

            button[kind = "tertiary"]:hover{
                transform : scale(1.05);
            }
            

        </style>

        """,
            unsafe_allow_html=True)



