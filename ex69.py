"""
Exercício Python 069: Crie um programa que leia
a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

pessoasComMaisDe18Anos = 0
homensCadastrados = 0
mulheresComMenosDe20Anos = 0

while (True):
    print("-=*"*15)
    print("CADASTRE UMA PESSOA")

    idade = int(input("Digite sua idade: "))

    sexo = " "
    while sexo not in "MF":
        sexo = input("Digite seu sexo [M/F]: ").upper().strip()[0]

    if idade >= 18:
        pessoasComMaisDe18Anos += 1
    if sexo == ("M"):
        homensCadastrados += 1
    if idade < 20 and sexo == ("F"):
        mulheresComMenosDe20Anos += 1

    print("-=*" * 15)

    opcao = " "
    while opcao not in "SN":
        opcao = input("Deseja continuar? [S/N]: ").upper().strip()[0]

    if opcao in ("S"):
        continue
    elif opcao == "N":
        print(f"{pessoasComMaisDe18Anos} pessoas são maiores de idades")
        print(f"{homensCadastrados} homens foram cadastrados ao total")
        print(f"Há {mulheresComMenosDe20Anos} mulheres com menos de 20 anos ")
        print("Programa Finalizado!")
        break