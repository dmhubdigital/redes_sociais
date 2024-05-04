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
palavras_chave = st.multiselect("Selecione até 50 palavras-chave:", [])
if st.button("Buscar Produtos"):
    if palavras_chave:
        for palavra_chave in palavras_chave:
            st.write(f"## Resultados para '{palavra_chave}':")
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
                st.write("Nenhum produto encontrado para esta palavra-chave.")
    else:
        st.warning("Por favor, selecione pelo menos uma palavra-chave para buscar produtos.")
