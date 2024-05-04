import requests
import schedule
import time
from tabulate import tabulate

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
            table = []
            for produto in produtos:
                frete_gratis = 'Sim' if 'shipping' in produto and produto['shipping']['free_shipping'] else 'Não'
                table.append([
                    produto['title'],
                    f"R${produto['price']:.2f}",
                    produto['permalink'],
                    f"![Thumbnail do Produto]({produto['thumbnail']})",
                    produto['reviews']['rating_average'] if 'reviews' in produto else '-',
                    produto['reviews']['total'] if 'reviews' in produto else '-',
                    frete_gratis
                ])
            print(tabulate(table, headers=['Nome', 'Preço', 'Link', 'Thumbnail', 'Nota', 'Avaliações', 'Frete Grátis'], tablefmt='grid'))
        else:
            print("Nenhum produto encontrado para esta palavra-chave.")

# Agendando a execução da função main a cada 1 minuto
schedule.every(1).minutes.do(main)

# Loop para executar a função main
while True:
    schedule.run_pending()
    time.sleep(1)
