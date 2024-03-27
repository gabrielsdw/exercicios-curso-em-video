"""
Exercício Python 075: Desenvolva um programa
que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite um número: "))
valor3 = int(input("Digite um número: "))
valor4 = int(input("Digite um número: "))
tupla = (valor1, valor2, valor3, valor4)

print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O primeiro valor 3 foi digitado na posição {tupla.index(3, 0)+1}")
else:
    print("O número 3 não foi digitado!")

pares = []

for c in tupla:
    if c % 2 == 0:
        pares.append(c)

print(f"os números pares foram {pares}")