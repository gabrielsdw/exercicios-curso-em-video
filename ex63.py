"""
Exercício Python 063: Escreva um programa que leia
um número N inteiro qualquer e mostre na tela os N
primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
"""

qntdElementos = int(input("Quantos elementos da sequência deseja ver? "))

a = [0,1,1]

i = 1
while i <= qntdElementos:
    numero = a[i] + a[i+1]
    a.append(numero)
    print(f"{i}° número: {a[i-1]}")
    i += 1









"""t1 = 0
t2 = 1
n = int(input("Quantos elementos da sequência deseja ver? "))

print(t1, t2, end=" ")
c = 3
while c <= n:
    t3 = t1 + t2
    print(t3, end=" ")
    t1 = t2
    t2 = t3
    c += 1"""

