"""
Exercício Python 098: Faça um programa que tenha uma
função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar
três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

def contador(inicio, fim, passo):
    print()
    passo = abs(passo)
    i = 1
    print("Contando de 1 à 10 de 1 em 1")
    while i <= 10:
        print(i, end=" ")
        i += 1
    print("=> FIM")
    print()
    print("Contando de 10 à 0 de 2 em 2")

    c = 10
    while c >= 0:
        print(c, end=" ")
        c -= 2
    print("=> FIM")
    print()
    print(f"Contando de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        i = inicio
        while i <= fim:
            print(i, end=" ")
            i += passo
    elif inicio > fim:
        i = inicio
        while i >= fim:
            print(i, end=" ")
            i -= passo
    else:
        print("Não existe contagem de números iguais")
    print("=> FIM")

inc = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))
passos = int(input("Digite os passos: "))
contador(inc, fim, passos)
