"""
Exercício Python 064: Crie um programa que leia
vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

i = 0
n = 0
soma = 0
while n != 999:
    n = int(input("Digite um número [999 para parar]: "))
    if n != 999:
        soma += n
        i += 1
print(f"A soma dos {i} números digitados é {soma}")







"""n = int(input("Digite um número [999 para parar]: "))
soma = i = 0
while n != 999:
    soma += n
    i += 1
    n = int(input("Digite um número [999 para parar]: "))"""
