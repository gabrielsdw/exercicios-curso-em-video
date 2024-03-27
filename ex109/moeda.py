def aumentar(n=0, p=0, formatacao=False):
    response = n + (n*p/100)
    return response if formatacao is False else moeda(response)


def diminuir(n=0, p=0, formatacao=False):
    response = n - (n*p/100)
    return response if not formatacao else moeda(response)


def dobro(n=0, formatacao=False):
    response = n*2
    return response if formatacao is False else moeda(response)


def metade(n=0, formatacao=False):
    response = n/2
    return response if formatacao == False else moeda(response)


def moeda(n=None, moeda="R$"):
    return f"{moeda}{n}".replace(".", ",")