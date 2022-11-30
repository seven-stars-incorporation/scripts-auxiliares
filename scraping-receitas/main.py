# Sites:
# https://www.minhasreceitas.com/
# https://receitas.globo.com/
# https://cybercook.com.br/


import requests
from bs4 import BeautifulSoup
from termcolor import colored

def linha():
    print(15*"=-"+"\n")

def conexao(url):        
    header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/51.0.2704.103 Safari/537.36'
            }
    
    global resp
    resp = requests.get(url, headers=header)

    if resp.status_code >= 200 and resp.status_code <= 299:
        return(resp)
    
    else:
        return(print("Erro na Conexão com "+url+"\nStatus: "+ resp.status_code))
        pass

# Só pega os links, pois nessas pesquisas aparecem noticias além de receita que são fora de padrão
# Se pesquisar OVO vem em um formato x; Pesquisando CARNE vem em formato Y......
def minhasreceitas(pqs):
    url = "https://www.minhasreceitas.com/search?q="+pqs
    conexao(url)

    soup = BeautifulSoup(resp.text, 'html.parser')

    lista_geral = soup.find(class_="grid-posts")

    lista_links = []

    for link in lista_geral.find_all('a'):

        lista_links.append(link.get('href'))
    
    print(lista_links)

# _______________________________________________________________________

def globoreceita(pqs):
    url = "https://receitas.globo.com/busca/?q="+pqs+"&order=relevant"
    conexao(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    print(colored("Receita encontrada!", 'green'))

    receita_geral = soup.find(class_='widget widget--card widget--info')
    receita_link_tag = receita_geral.find('a')

    link_real = receita_link_tag['href']
    link_real = "https:"+link_real

    conexao(link_real)
    soup = BeautifulSoup(resp.text, 'html.parser')
    link_real = soup.find('script')
    link_real = str(link_real)

    link_real = link_real.replace('<script>window.location.replace("', '')
    link_real = link_real.replace('");</script>', '')

    conexao(link_real)
    soup = BeautifulSoup(resp.text, 'html.parser')

    receita_nome = soup.find('h1', attrs={"class":"content-head__title"}).get_text()
    print(colored("Nome da Receita: ", 'yellow')+receita_nome)

    receita_categoria = soup.find('a', attrs={"class":"entities__list-itemLink"}).get_text()
    print("Categoria: "+ receita_categoria)

    print("\nIngredientes: ")
    receita_ingredientes = soup.find('ul', attrs={"class":"content-unordered-list"})

    for ingredientes in receita_ingredientes:
        print(ingredientes.get_text())

    receita_preparo = soup.find_all('span', attrs={"class":"recipeInstruction__text"})

    receita_preparo = str(receita_preparo)
    receita_preparo = receita_preparo.replace('<span class="recipeInstruction__text">', "")
    receita_preparo = receita_preparo.replace('</span>', "\n")
    receita_preparo = receita_preparo.replace('[', "")
    receita_preparo = receita_preparo.replace(']', "")

    print(receita_preparo)

    linha()

    # for preparo in receita_preparo:
    #     print(preparo, end="\n ")


# _______________________________________________________________________
def cybercook(pqs):
    url = "https://cybercook.com.br/search?q="+pqs+"&is_premium=true&calorias=0&custo=0&prep=0"
    conexao(url)

    soup = BeautifulSoup(resp.text, 'html.parser')

    print(colored("Receita encontrada!", 'green'))

    link_receita = soup.find(class_='pos-relative border-card-half-2 grid-sm-12 font-serif grid-lg-4 mb5 card--half-2-image')
    link_receita = link_receita.find('a')
    link_receita = link_receita['href']
    link_receita = "https://cybercook.com.br"+link_receita

    conexao(link_receita)
    soup = BeautifulSoup(resp.text, 'html.parser')

    receita_nome = soup.find('h1').string
    print(colored("Nome da Receita: ", 'yellow')+receita_nome)

    receita_categoria = soup.find('div', attrs={"class":"flex flex-wrap undefined"}).get_text()
    print("Categorias: "+receita_categoria)

    receita_ingrediente = soup.find('h2')
    print("Ingredientes:\n")
    for ingredientes in receita_ingrediente.find_all_next('label'):
        print(">> "+ingredientes.get_text())


    receita_preparo = soup.find('ul', attrs={"class":"custom-counter"})
    print("\nModo de preparo: ")
    for preparo in receita_preparo:
        print(preparo.get_text())


# _______________________________________________________________________

banner = '''
  /$$$$$$  /$$$$$$$$ /$$    /$$ /$$$$$$$$ /$$   /$$        /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$   /$$$$$$ 
 /$$__  $$| $$_____/| $$   | $$| $$_____/| $$$ | $$       /$$__  $$|__  $$__//$$__  $$| $$__  $$ /$$__  $$
| $$  \__/| $$      | $$   | $$| $$      | $$$$| $$      | $$  \__/   | $$  | $$  \ $$| $$  \ $$| $$  \__/
|  $$$$$$ | $$$$$   |  $$ / $$/| $$$$$   | $$ $$ $$      |  $$$$$$    | $$  | $$$$$$$$| $$$$$$$/|  $$$$$$ 
 \____  $$| $$__/    \  $$ $$/ | $$__/   | $$  $$$$       \____  $$   | $$  | $$__  $$| $$__  $$ \____  $$
 /$$  \ $$| $$        \  $$$/  | $$      | $$\  $$$       /$$  \ $$   | $$  | $$  | $$| $$  \ $$ /$$  \ $$
|  $$$$$$/| $$$$$$$$   \  $/   | $$$$$$$$| $$ \  $$      |  $$$$$$/   | $$  | $$  | $$| $$  | $$|  $$$$$$/
 \______/ |________/    \_/    |________/|__/  \__/       \______/    |__/  |__/  |__/|__/  |__/ \______/ 
                                                                                                          
                                                                                                          \n
'''
info = '''
                [+] Pesquisa semi-automática para demonstração
'''

print(colored(banner, 'blue'), colored(info, 'yellow'))
pqs = input("Pesquisa: ")
print("\nPesquisando...\n")
pqs = pqs.replace(" ", "%20")
pqs = pqs.replace("ç" or "Ç", "%C3%A7")
pqs = pqs.replace("á" or "Á", "%C3%A1")
pqs = pqs.replace("à" or "À", "%C3%A0")
pqs = pqs.replace("é" or "É", "%C3%A9")
pqs = pqs.replace("è" or "È", "%C3%A8")
pqs = pqs.replace("ã" or "Ã", "%C3%A3")
pqs = pqs.replace("õ" or "Õ", "%C3%B5")


# minhasreceitas(pqs)
globoreceita(pqs)
cybercook(pqs)