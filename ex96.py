"""
Exercício Python 096: Faça um programa que tenha uma
função chamada área(), que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

def area(largura, comprimento):
    print(f"A área do terreno é de {largura*comprimento} m².")

l = float(input("Digite a largura: "))
c = float(input("Digite o comprimento: "))
area(l, c)