def aumentar(n=0, p=0):
    return n + (n*p/100)


def diminuir(n=0, p=0):
    return n - (n*p/100)


def dobro(n=0):
    return n*2


def metade(n=0):
    return n/2


def moeda(n=0, moeda="R$"):
    return f"{moeda}{n}".replace(".", ",")