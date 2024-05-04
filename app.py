import streamlit as st
import requests

# Função para buscar produtos no Mercado Livre
def buscar_produtos(palavra_chave):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={palavra_chave}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        return None

# Interface do Streamlit
st.title("Extrator de Produtos do Mercado Livre")

# Entrada do usuário
palavra_chave = st.text_input("Digite o nome do produto ou palavra-chave:")
if st.button("Buscar Produtos"):
    if palavra_chave:
        st.write(f"Buscando produtos relacionados à '{palavra_chave}'...")
        produtos = buscar_produtos(palavra_chave)
        if produtos:
            st.write(f"Total de produtos encontrados: {len(produtos)}")
            for produto in produtos:
                st.write("---")
                st.write(f"**Nome:** {produto['title']}")
                st.write(f"**Preço:** R${produto['price']:.2f}")
                st.write(f"**Link:** {produto['permalink']}")
                st.image(produto['thumbnail'], caption='Thumbnail do Produto', use_column_width=True)
        else:
            st.write("Nenhum produto encontrado.")
    else:
        st.warning("Por favor, insira uma palavra-chave para buscar produtos.")
