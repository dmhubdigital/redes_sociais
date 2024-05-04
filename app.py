import streamlit as st

st.title("Extrator de Produtos do Mercado Livre")

palavras_chave = st.text_input("Digite as palavras-chave separadas por vírgula:")
if st.button("Buscar Produtos"):
    if palavras_chave:
        st.write("A busca será realizada automaticamente. Por favor, aguarde...")
    else:
        st.warning("Por favor, insira pelo menos uma palavra-chave para buscar produtos.")
