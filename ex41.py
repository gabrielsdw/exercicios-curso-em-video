"""Exercício Python 041: A Confederação Nacional de Natação precisa
   de um programa que leia o ano de nascimento de um atleta e
   mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

from datetime import date

anoDeNascimento = int(input("Digite seu ano de nascimento: "))
anoAtual = date.today().year
idade = anoAtual-anoDeNascimento

if idade <= 9:
    categoria = "Mirim"

elif idade <= 14:
    categoria = "Infantil"

elif idade <= 19:
    categoria = "Júnior"

elif idade <= 25:
    categoria = "Sênior"

else:
    categoria = "Master"

print(f"Quem tem {idade} anos é {categoria}")