"""
Exercício Python 094: Crie um programa que leia nome,
sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

dicionario = dict()
lista = list()
while True:
    nome = str(input("Digite seu nome: "))
    sexo = str(input("Digite seu sexo: "))
    idade = int(input("Digite a sua idade: "))
    dicionario["nome"] = nome
    dicionario["sexo"] = sexo
    dicionario["idade"] = idade
    lista.append(dicionario.copy())
    dicionario.clear()
    continuar = input("Deseja continuar? [S/N]: ").strip().lower()[0]
    if continuar == "n":
        break

print("-="*30)
print(f"A) {len(lista)} pessoas foram cadastradas")
print("-="*30)

i = 0
somaIdade = 0
mediaIdade = 0
while i < len(lista):
    somaIdade += lista[i]["idade"]
    i += 1
mediaIdade = somaIdade/len(lista)

print(f"B) A média de idade é {mediaIdade:.2f}")
print("-="*30)

listaMulheres = list(filter(lambda x: x['sexo'].lower().strip()[0] == "f", lista))
listaPessoasIdadeAcimaDaMedia = list(filter(lambda x: x['idade'] > mediaIdade, lista))

print(f"C) Mulheres cadastradas: ")
for i in range(len(listaMulheres)):
    print(f"{listaMulheres[i]['nome']}")
print("-="*30)

print(f"D) Pessoas com Idade acima da Média:")
for c in range(len(listaPessoasIdadeAcimaDaMedia)):
    print(f"{listaPessoasIdadeAcimaDaMedia[c]['nome']}")
print("-="*30)