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

# Cria o comando da barra lateral no streamlit
with st.sidebar:
    # Define o título da barra lateral
    st.title("🤖 Ramos AI Coder")
    #Mostra um texto explicativo sobre o assistente 
    st.markdown("Um assistente de IA focado em programação Python para ajudar iniciantes.")

    # Campo para inserir a chave API da Groq
    groq_api_key = st.text_input(
        "Insira sua API Groq",
        type="password",
        help="Obtenha sua chave em Groq"
    )
    
    # Adiciona Linhas divisórias e explicações extras na barra lateral
    st.markdown("-----")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com linguagem Python. A IA pode cometer erros. Sempre verifique as respostas.")
    st.markdown("-----")
    st.markdown("Conheças mais dos meus projetos em meu perfil.")

    # Link para o meu perfil
    st.markdown("🔗[Ramos Code](https://github.com/kaia-boo)")
    # Botão de link para enviar ao suporte
    st.link_button("E-mail para o suporte no Caso de dúvidas", "linkdoemailaqui")

# Título principal do App
st.title(" Kaia-Boo - RAMOS AI CODER 💻")

# Subtítulo adicional
st.title(" 🐍 Assistente Pessoal de Programação Python 🐍 ")

# Texto auxiliar abaixo do título
st.caption("Faça sua pergunta sobre linguagem Python e obtenha código, explicações e referências.")

# Inicia o Histórico de mensagens na sessão, caso ainda não exista 
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir todas as mensagens anteriores armazenadas no estado da sessão
for mesage in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
