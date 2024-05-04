import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

# Função para extrair os resultados da pesquisa do YouTube
def extrair_resultados_youtube(termo):
    try:
        url = f"https://www.youtube.com/results?search_query={termo}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("div", class_="style-scope ytd-video-renderer")
        return results
    except Exception as e:
        st.error(f"Erro ao extrair resultados do YouTube: {e}")

# Função para extrair o número de inscritos do canal
def extrair_inscritos_canal(canal):
    try:
        inscritos = canal.find("yt-formatted-string", class_="style-scope ytd-channel-renderer")
        if inscritos:
            return inscritos.text.strip()
        else:
            return "N/A"
    except Exception as e:
        st.error(f"Erro ao extrair número de inscritos do canal: {e}")

# Função para extrair o tempo desde a publicação do vídeo
def extrair_tempo_publicacao(tempo):
    try:
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
    except Exception as e:
        st.error(f"Erro ao extrair tempo de publicação do vídeo: {e}")

# Configurações da aplicação Streamlit
st.title("Extrator de Resultados do YouTube")

# Campo de texto para o usuário inserir o termo de pesquisa
termo_pesquisa = st.text_input("Insira o termo de pesquisa do YouTube:")

# Botão para iniciar a pesquisa
if st.button("Buscar"):
    if termo_pesquisa:
        resultados = extrair_resultados_youtube(termo_pesquisa)
        if resultados:
            st.write("Resultados:")
            for resultado in resultados:
                try:
                    titulo = resultado.find("a", {"id": "video-title"}).text.strip()
                    visualizacoes = resultado.find("span", {"class": "style-scope ytd-video-meta-block"}).text.strip()
                    canal = resultado.find("a", {"class": "yt-simple-endpoint style-scope yt-formatted-string"}).text.strip()
                    inscritos = extrair_inscritos_canal(resultado.find("div", {"id": "channel-info"}))
                    tempo_publicacao = resultado.find("span", {"class": "style-scope ytd-video-meta-block"}).text.strip()
                    tempo_publicacao = extrair_tempo_publicacao(tempo_publicacao)
                    st.write(f"Título: {titulo}")
                    st.write(f"Visualizações: {visualizacoes}")
                    st.write(f"Canal: {canal}")
                    st.write(f"Inscritos: {inscritos}")
                    st.write(f"Tempo desde a publicação: {tempo_publicacao}")
                    st.write("---")
                except Exception as e:
                    st.error(f"Erro ao processar resultado: {e}")
        else:
            st.write("Nenhum resultado encontrado.")
    else:
        st.write("Por favor, insira um termo de pesquisa.")
