"""
Exercício Python 061: Refaça o DESAFIO 051,
lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while
"""

primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

i = 0
while i < 10:
    print(primeiroTermo)
    primeiroTermo += razao
    i += 1