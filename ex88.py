"""
Exercício Python 088: Faça um programa que ajude
um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""

from random import randint

palpites = []
jogos = []

qntdJogos = int(input("Deseja fazer quantos jogos? "))

for i in range(0, qntdJogos):
    for j in range(1,7):
        palpites.append(randint(0,60))
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()

for k, v in enumerate(jogos, 1):
    print(f"{k}° jogo: {v}")

"""k = 0
while k < len(jogos):
    print(f"{k+1}° jogo: {jogos[k]}")
    k += 1
"""