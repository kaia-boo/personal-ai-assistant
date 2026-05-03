# Assistente de programação em Python

# Importa módulo para interagir com o sistema operacional
import os 

# Importa a biblioteca Streamlit para criar interface web interativa
import streamlit as st

# Importa a classe Groq para conectar à API da plataforma Groq
from groq import Groq

# Configura a página do Streamlit
st.set_page_config(
    page_title="Ramos AI Coder",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
