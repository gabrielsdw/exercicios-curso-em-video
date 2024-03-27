"""
Exercício Python 060: Faça um programa que
leia um número qualquer e mostre o seu fatorial.
"""

numero1 = int(input('Digite um número para saber o seu fatorial: '))
f1 = 1
c1 = numero1
while c1 > 1:
    f1 *= c1
    c1 -= 1
print(f'O resultado de {numero1}! é  {f1}')