"""
Exercício Python 055: Faça um programa que leia
o peso de cinco pessoas. No final, mostre qual
foi o maior e o menor peso lidos.
"""
maiorPeso = 0
menorPeso = 0


for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}º pessoa: "))
    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

print(f"O maior peso informado foi {maiorPeso}Kg e o menor {menorPeso}Kg")

