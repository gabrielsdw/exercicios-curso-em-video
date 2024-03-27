"""
Exercício Python 054: Crie um programa que leia
o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

maioresDeIdade = 0
menoresDeIdade = 0

for i in range(1, 8):
    anoDeNascimento = int(input(f"Digite o ano de nascimento da {i}° pessoa: "))
    idade = date.today().year - anoDeNascimento
    if idade >= 21:
        maioresDeIdade += 1
    else:
        menoresDeIdade += 1

print(f"{maioresDeIdade} pessoas são maiores de idade\n"
      f"{menoresDeIdade} pessoas são menores de idade")


