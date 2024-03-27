"""
Exercício Python 114: Crie
um código em Python que teste
se o site pudim está acessível
pelo computador usado.
"""


def verificaAcesso(url):
    import requests
    try:
        if requests.get(url).status_code == 200:
            print("Está acessível")
    except:
        print("Não está acessível")



url = "http://www.pudim.com.br"
verificaAcesso(url)