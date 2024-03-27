"""
Exercício Python 067: Faça um programa que mostre
a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.
"""

while True:
    n = int(input("Digite um número: "))
    if n > 0:
        i = 1
        while i <= 10:
            print(f'{n}x{i}={n*i}')
            i += 1
    else:
        print("Programa Finalizado!")
        break
