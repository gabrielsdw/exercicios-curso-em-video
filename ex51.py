"""
Exercício Python 051: Desenvolva um programa
que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

primeiroTermo = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
termos = float()

for c in range(primeiroTermo, (primeiroTermo+10*r), r):
    print(c, end=" ")
