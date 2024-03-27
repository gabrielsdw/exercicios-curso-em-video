"""
Exercício Python 086: Crie um programa que declare
uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz na tela,
com a formatação correta.
"""

matriz = [[],[],[]]

for i in range(1, 10):
    numero = int(input('Digite um número: '))
    if i <= 3:
        matriz[0].append(numero)
    elif i <= 6:
        matriz[1].append(numero)
    else:
        matriz[2].append(numero)

for c in matriz:
    print(c)


"""
for c in range(0,3):
    for j in range(0,3):
        matriz[c][j] = (int(input("Digite um número: ")))

for c in matriz:
    print(c)
"""