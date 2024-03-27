"""
Exercício Python 101: Crie um programa que
tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""

def voto(anoDeNascimento):
    """
    Função que define a situação de seu voto de acordo com sua idade
    :param anoDeNascimento: Ano de nascimento da pessoa
    :return: retorna a situação de voto da pessoa
    Feito por: Gabriel Oliveira Santos
    """

    from datetime import date
    idade = date.today().year - anoDeNascimento
    if idade < 16:
        return f"Com {idade} anos o seu voto é Negado"
    elif idade >= 16 and idade < 18 or idade > 65:
        return f"Com {idade} anos o seu voto é Opcional"
    else:
        return f"Com {idade} anos o seu voto é Obrigatório"

anoDeNascimento = int(input("Digite o seu ano de nascimento: "))
print(voto(anoDeNascimento))