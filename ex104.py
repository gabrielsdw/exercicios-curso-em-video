"""
Exercício Python 104: Crie um programa que tenha
a função leiaInt(), que vai funcionar de forma
semelhante 'a função input() do Python, só que
fazendo a validação para aceitar apenas um valor numérico.

Ex: n = leiaInt('Digite um n: ')
"""

def leiaInt(texto=""):
    """
    -> Função que força o usuário a digitar um número inteiro
    :param texto: texto que pede a digitação do usuário
    :return: retorna o número inteiro digitado pelo usuário
    Feito por Gabriel Oliveira Santos
    """
    while True:
        n = input(texto)
        if n.isnumeric():
            break
    return n


numero = leiaInt("Digite um número inteiro: ")
print(numero)