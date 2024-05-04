
import streamlit as st
import requests
from bs4 import BeautifulSoup
import mysql.connector 

# Função para extrair os resultados da pesquisa do YouTube
def extrair_resultados_youtube(termo):
    url = f"https://www.youtube.com/results?search_query={termo}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    resultados = soup.find_all("h3", {"class": "title-and-badge style-scope ytd-video-renderer"})
    return [resultado.text.strip() for resultado in resultados]

# Função para conectar ao banco de dados MySQL
def conectar_mysql():
    return mysql.connector.connect(
        host="seu_host",
        user="seu_usuario",
        password="sua_senha",
        database="seu_banco_de_dados"
    )

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
            st.write(resultado)
    else:
        st.write("Por favor, insira um termo de pesquisa.")




# Exemplo de código para inserir dados no banco de dados
# cursor = conexao.cursor()
# cursor.execute("INSERT INTO tabela (coluna1, coluna2) VALUES (%s, %s)", (valor1, valor2))
# conexao.commit()
# st.write("Dados inseridos no banco de dados.")
# cursor.close()
# conexao.close()
