"""
Exercício Python 057: Faça um programa
que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação
novamente até ter um valor correto.
"""

i = 0
c = 0

sexo = input("Digite um sexo (M) or (F): ").strip().upper()[0]

while sexo not in "FM":
    sexo = input("Dados Inválidos! Digite novamente: ").upper()[0]

print("Operação feita com sucesso!")