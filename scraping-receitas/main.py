# Sites:
# https://www.minhasreceitas.com/
# https://www.receiteria.com.br/
# https://www.receitasetemperos.com.br/
# 

from conexao_url import conexao
from bs4 import BeautifulSoup

def minhasreceitas():
    url = "https://www.minhasreceitas.com/"
    conexao(url)


minhasreceitas()