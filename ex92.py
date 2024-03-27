"""
Exercício Python 092: Crie um programa
que leia nome, ano de nascimento e carteira
de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário
receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date

cadastro = dict()
cadastro["nome"] = str(input("Digite seu nome: "))
anoDeNascimento = int(input("Digite o ano de seu nascimento: "))
cadastro["idade"] = date.today().year-anoDeNascimento
cadastro["ctps"] = int(input("Carteira de Trabalho (0) não tem: "))

if cadastro["ctps"] != 0:
    cadastro["anoDeContratação"] = int(input("Digite o ano de contratação: "))
    cadastro["salario"] = int(input("Digite o seu salário: R$"))
    cadastro["aposentadoria"] = cadastro["idade"] + ((cadastro["anoDeContratação"] + 35) - date.today().year)

for keys, values in cadastro.items():
    print(f"{keys} tem o valor {values}")