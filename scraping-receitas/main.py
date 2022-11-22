# Sites:
# https://www.minhasreceitas.com/
# https://www.receiteria.com.br/
# https://www.receitasetemperos.com.br/
# 
import requests
from bs4 import BeautifulSoup

def conexao(url):        
    header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/51.0.2704.103 Safari/537.36'
            }
    
    global resp
    resp = requests.get(url, headers=header)

    if resp.status_code == 200:
        return(resp)
    
    else:
        return(print("Erro na Conexão\nStatus: "+ resp.status_code))
        exit()

def minhasreceitas(pqs):
    url = "https://www.minhasreceitas.com/search?q="+pqs
    conexao(url)

    soup = BeautifulSoup(resp.text, 'html.parser')

    lista_geral = soup.find('')




minhasreceitas()