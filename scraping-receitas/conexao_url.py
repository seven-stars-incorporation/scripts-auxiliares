import requests


def conexao(url):        
    header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/51.0.2704.103 Safari/537.36'
            }
    
    resp = requests.get(url, headers=header)

    if resp.status_code == 200:
        return(print("Conexão OK"))
    
    else:
        return(print("Erro na Conexão\nStatus: "+ resp.status_code))
        exit()