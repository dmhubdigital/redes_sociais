import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

# Função para extrair os resultados da pesquisa do YouTube
def extrair_resultados_youtube(termo):
    url = f"https://www.youtube.com/results?search_query={termo}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    resultados = soup.find_all("div", {"class": "text-wrapper style-scope ytd-video-renderer"})
    return resultados

# Função para extrair o número de inscritos do canal
def extrair_inscritos_canal(canal):
    inscritos = canal.find("span", {"class": "style-scope ytd-channel-renderer"})
    if inscritos:
        return inscritos.text.strip()
    else:
        return "N/A"

# Função para extrair o tempo desde a publicação do vídeo
def extrair_tempo_publicacao(tempo):
    tempo_str = tempo.text.strip()
    if "ago" in tempo_str:
        tempo_str = re.sub("[^0-9]", "", tempo_str)
        tempo_int = int(tempo_str)
        if "hour" in tempo.text:
            return f"{tempo_int} horas atrás"
        elif "day" in tempo.text:
            return f"{tempo_int} dias atrás"
        elif "week" in tempo.text:
            return f"{tempo_int} semanas atrás"
        elif "month" in tempo.text:
            return f"{tempo_int} meses atrás"
        elif "year" in tempo.text:
            return f"{tempo_int} anos atrás"
    else:
        return tempo_str

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
            titulo = resultado.find("a", {"id": "video-title"})
            visualizacoes = resultado.find("span", {"class": "style-scope ytd-video-meta-block"})
            canal = resultado.find("div", {"id": "channel-info"})
            inscritos = extrair_inscritos_canal(canal)
            tempo_publicacao = resultado.find("span", {"class": "style-scope ytd-video-meta-block"})
            tempo_publicacao = extrair_tempo_publicacao(tempo_publicacao)
            st.write(f"Título: {titulo.text.strip()}")
            st.write(f"Visualizações: {visualizacoes.text.strip()}")
            st.write(f"Canal: {canal.text.strip()}")
            st.write(f"Inscritos: {inscritos}")
            st.write(f"Tempo desde a publicação: {tempo_publicacao}")
            st.write("---")
    else:
        st.write("Por favor, insira um termo de pesquisa.")
