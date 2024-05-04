import streamlit as st
import instaloader

def extrair_metricas(usuario):
    # Inicializa o instaloader
    loader = instaloader.Instaloader()

    try:
        # Carrega o perfil do usuário
        profile = instaloader.Profile.from_username(loader.context, usuario)

        # Extrai as métricas
        seguidores = profile.followers
        num_posts = profile.mediacount

        # Calcula a média de curtidas e comentários por post
        total_curtidas = 0
        total_comentarios = 0
        for post in profile.get_posts():
            total_curtidas += post.likes
            total_comentarios += post.comments
        media_curtidas = total_curtidas / num_posts if num_posts > 0 else 0
        media_comentarios = total_comentarios / num_posts if num_posts > 0 else 0

        return seguidores, num_posts, media_curtidas, media_comentarios

    except instaloader.exceptions.ProfileNotExistsException:
        st.error("O perfil não existe.")
        return None

# Interface do Streamlit
st.title("Extrator de Métricas do Instagram")
usuario = st.text_input("Digite o nome de usuário do Instagram:")

if st.button("Extrair Métricas"):
    if usuario:
        # Extrai as métricas
        metricas = extrair_metricas(usuario)
        if metricas:
            seguidores, num_posts, media_curtidas, media_comentarios = metricas

            # Exibe as métricas
            st.write(f"Seguidores: {seguidores}")
            st.write(f"Número de Posts: {num_posts}")
            st.write(f"Média de Curtidas por Post: {media_curtidas:.2f}")
            st.write(f"Média de Comentários por Post: {media_comentarios:.2f}")
    else:
        st.warning("Por favor, insira um nome de usuário do Instagram.")
