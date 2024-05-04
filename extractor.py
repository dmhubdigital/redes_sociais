import requests
import schedule
import time

# Função para buscar produtos no Mercado Livre
def buscar_produtos(palavra_chave):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={palavra_chave}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        return None

# Função principal da aplicação
def main():
    palavras_chave = ["celular", "notebook", "smartwatch"]  # Exemplo de palavras-chave
    for palavra_chave in palavras_chave:
        print(f"Resultados para '{palavra_chave}':")
        produtos = buscar_produtos(palavra_chave)
        if produtos:
            print(f"Total de produtos encontrados: {len(produtos)}")
            for produto in produtos:
                print("---")
                print(f"Nome: {produto['title']}")
                print(f"Preço: R${produto['price']:.2f}")
                print(f"Link: {produto['permalink']}")
        else:
            print("Nenhum produto encontrado para esta palavra-chave.")

# Agendando a execução da função main a cada 1 minuto
schedule.every(1).minutes.do(main)

# Loop para executar a função main
while True:
    schedule.run_pending()
    time.sleep(1)
