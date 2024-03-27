"""
Exercício Python 089: Crie um programa que
leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada
um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
"""
dados = []
lista = []

while True:
    nome = input('Digite seu nome: ')
    nota1 = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite a sua segunda nota: '))
    continuar = input("Deseja continuar? {S/N} ").strip().lower()[0]
    print("-="*30)
    #lista.append([nome, [nota1, nota2], media])
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    lista.append(dados[:])
    dados.clear()
    if continuar == "n":
        break

for k in range(0, len(lista)):
    media = (lista[k][1] + lista[k][2]) / 2
    print(f"{k+1}° pessoa: {lista[k][0]},  Média: {media}")


while True:
    aluno = int(input("Mostrar notas de qual Aluno? [digite 999 para parar]: "))
    if aluno == 999:
        print("Programa Finalizado!")
        break
    print(f"Notas de {lista[aluno-1][0]}: {lista[aluno-1][1:3]}")