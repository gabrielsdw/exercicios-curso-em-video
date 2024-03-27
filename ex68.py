"""
Exercício Python 068: Faça um programa que jogue
par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""

from random import randint

i = 0
while True:

    computador = randint(0,10)
    print(computador)
    jogador = int(input("Digite um número: "))
    escolhaJogador = input("Ímpar ou Par? [p/i]: ").lower().strip()[0]

    soma = computador + jogador

    if soma % 2 == 0 and escolhaJogador == "p" or soma % 2 != 0 and escolhaJogador == "i":
        i += 1
        print("O jogador Ganhou")

        if soma % 2 == 0:
            print(f"A soma de {computador} + {jogador} é  {soma} e é par")
        else:
            print(f"A soma de {computador} + {jogador} é {soma} e é ímpar")

        soma = 0

    else:
        print("\n")
        print(f"O jogador teve {i} vitórias")
        print(f"O jogador perdeu!")
        print("Fim do jogo!")
        break

