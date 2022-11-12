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