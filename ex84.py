"""
Exercício Python 084: Faça um programa que leia
nome e peso de várias pessoas, guardando tudo em
uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

lista = []
dados = []
while (True):
    nome = input("Digite seu nome: ")
    dados.append(nome)
    peso = float(input("Digite seu peso: "))
    dados.append(peso)
    lista.append(dados[:])
    dados.clear()
    continuar = input("Deseja continuar? ").lower().strip()[0]
    if continuar == "n":
        break


maior = menor = 0
for k, v in enumerate(lista, 1):
    if k == 1:
        maior = menor = v[1]
    else:
        if v[1] > maior:
            maior = v[1]
        if v[1] < menor:
            menor = v[1]

print(f"{len(lista)} pessoas foram cadastradas")

nomePessoaMaisPesada = str()
for pessoa in lista:
    if pessoa[1] == maior:
        nomePessoaMaisPesada = pessoa[0]

nomePessoaMaisLeve = str()
for pessoa in lista:
    if pessoa[1] == menor:
        nomePessoaMaisLeve = pessoa[0]

print(f"A pessoa mais pesada é {nomePessoaMaisPesada} e ela tem {maior} Kg")
print(f"A pessoa mais leve é {nomePessoaMaisLeve} e ela tem {menor} Kg")