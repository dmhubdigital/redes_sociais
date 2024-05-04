import streamlit as st
import requests
from bs4 import BeautifulSoup

# Função para extrair os resultados da pesquisa do YouTube
def extrair_resultados_youtube(termo):
    url = f"https://www.youtube.com/results?search_query={termo}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    resultados = soup.find_all("h3", {"class": "title-and-badge style-scope ytd-video-renderer"})
    return resultados

# Configurações da aplicação Streamlit
st.title("Extrator de Resultados do YouTube")

# Campo de texto para o usuário inserir o termo de pesquisa
termo_pesquisa = st.text_input("Insira o termo de pesquisa do YouTube:")

# Botão para iniciar a pesquisa
if st.button("Buscar"):
    if termo_pesquisa:
        resultados = extrair_resultados_youtube(termo_pesquisa)
        st.write("Resultados:")
        for resultado in resultados:
            st.write(resultado.text.strip())
    else:
        st.write("Por favor, insira um termo de pesquisa.")
