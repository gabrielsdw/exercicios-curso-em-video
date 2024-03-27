"""
Exercício Python 056: Desenvolva um programa que leia o nome,
idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.
"""

somaIdade = 0
mulheresMenorDe20 = 0

for c in range(1, 5):
    print("=-"*11, c)
    nome = input("Digite seu nome: ")
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite seu sexo (M) or (F): ").upper()[0]
    somaIdade += idade
    if c == 1 and sexo == "M":
        homemMaisVelho = nome
        idadeHomemMaisVelho = idade
    else:
        if idade > idadeHomemMaisVelho and sexo == "M":
            idadeHomemMaisVelho = idade
            homemMaisVelho = nome
    if sexo == "F" and idade < 20:
        mulheresMenorDe20 += 1

print(f"A média das idades é de {somaIdade/4}")
print(f"O homem mais velho tem {idadeHomemMaisVelho} anos e ele se chama {homemMaisVelho}")
print(f"Existem {mulheresMenorDe20} mulheres com menos de 20 anos")
