"""
Exercício Python 099: Faça um programa que
tenha uma função chamada maior(), que receba
vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores
e dizer qual deles é o maior.
"""

def maior(*num):
    maior = 0
    for value in num:
        if value > maior:
            maior = value
    return maior

print(maior(0, 8, 11, 10.5, 16, 16.1))
