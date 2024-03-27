"""
Exercício Python 102: Crie um programa que
tenha uma função fatorial() que receba dois
parâmetros: o primeiro que indique o número a
calcular e outro chamado show, que será um valor
lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial.
"""

def fatorial(numero, show=None):
    """
    -> Função que calcula o fatorial de um numero N
    :param numero: Numero a ser calculado o fatorial
    :param show: Mostrar ou não a conta feita
    :return: retorna o fatorial do número
    Feito por Gabriel Oliveira Santos
    """
    if show:
        fatorial = 1
        while numero > 0:
            fatorial *= numero
            print(numero, end=" ")
            print("x" if numero > 1 else f"=> {fatorial}", end=" ")
            numero -= 1
        return fatorial

    else:
        fatorial = 1
        for c in range(numero, 0, -1):
            fatorial *= c
        return fatorial

print(fatorial(5))