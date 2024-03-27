"""Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date

anoAtual = date.today().year
anoDeNascimento = int(input("Digite o ano em que você nasceu: "))
idade = anoAtual-anoDeNascimento

if idade < 18:
    print(f"Você ainda vai se alistar\n"
          f"Quem nasceu em {anoDeNascimento} tem {idade} anos em {anoAtual}\n"
          f"falta {18-idade} anos para você se alistar!\n"
          f"Você se alistará em {anoDeNascimento+18}")
elif idade > 18:
    print("Você já deveria ter se alistado\n"
          f"Quem nasceu em {anoDeNascimento} tem {idade} anos em {anoAtual}\n"
          f"Você está atrasado em {idade-18} anos\n"
          f"Você deveria ter se alistado em {(anoAtual-idade)+18}")
else:
    print("Você está com a idade exata para se alistar!")
