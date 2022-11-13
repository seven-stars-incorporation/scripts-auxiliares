# Pesquisa de preço de produtos do mercado.
# Preciso de Header, converter a stinrg pra url válida, fazer a pesquisa... éh isso
import requests
from bs4 import BeautifulSoup

def pesquisa():
    header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/51.0.2704.103 Safari/537.36'
        }
    
    pqs = input("Produto: ")
    url = 'https://www.zonasul.com.br/'+pqs

    resp = requests.get(url, headers=header)

    if resp.status_code == 200:
        
        soup = BeautifulSoup(resp.text, 'html.parser')

        produto_tag = soup.find('article')

        produto_preco = produto_tag.find(class_='zonasul-zonasul-store-0-x-currencyContainer')
        produto_preco = produto_preco.get_text()

        produto_preco = produto_preco.replace("R$", "")
        # produto_preco = float(produto_preco)

        # print(type(produto_preco))

        produto_nome = produto_tag.find('span')
        produto_nome = produto_nome.get_text()

        print("\n"+"="*15+"\n"+produto_nome+"\n"+str(produto_preco)+"\n")

    else:   
        print("Falha na requisição.\nCod de retorno: "+resp.status_code)


pesquisa()