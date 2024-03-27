"""
Exercício Python 058: Melhore o jogo do DESAFIO 028
onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint

computador = randint(0, 10)
jogador = int(input("Digite um número entre 0 e 10: "))
palpites = 1

while jogador != computador:
    jogador = int(input("Você errou!! Tente Novamente: "))
    palpites += 1
    if jogador == computador:
        print(f"Você acertou!!!")
    else:
        if jogador < computador:
            print("Maisss")
        else:
            print("Menosss")

print(f"Foram necessários {palpites} palpites para vencer da máquina!")