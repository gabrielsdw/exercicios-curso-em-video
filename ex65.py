"""
Exercício Python 065: Crie um programa que leia
vários números inteiros pelo teclado. No final da
execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores.
"""

condicao = True
soma = 0
i = 0
maior = 0
menor = 0
while condicao == True:

    numero = int(input("Digite um número: "))
    opcao = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
    soma += numero
    i += 1

    if opcao == "s":

        if i == 1:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero

    else:
        print(f"A média de todos os números digitados é {soma/i}")
        print(f"O maior número é {maior} e o menor {menor}")
        condicao = False