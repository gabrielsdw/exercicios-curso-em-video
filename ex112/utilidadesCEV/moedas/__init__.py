def aumentar(n=0, p=0, formatacao=False):
    """
    << Função que aumenta X porcentagem em um valor N >>
    :param n: valor N a ser usado
    :param p: porcentagem X a ser usada
    :param formatacao: Devolve ou não o valor formatado
    :return: valor reajustado, com ou sem formatação
    """

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


def resumo(n=0, porcentagemAumento=0, porcentagemReducao=0):
    print(f"Preço analisado: {moeda(n)}")
    print(f"Dobro do preço: {dobro(n, formatacao=True)}")
    print(f"Metade do preço: {metade(n, formatacao=True)}")
    print(f"{porcentagemAumento}% de aumento: {aumentar(n, porcentagemAumento, formatacao=True)}")
    print(f"{porcentagemReducao}% de redução: {diminuir(n, porcentagemReducao, formatacao=True)}")