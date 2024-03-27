"""
Exercício Python 091: Crie um programa onde 4 jogadores
joguem um dado e tenham resultados aleatórios. Guarde
esses resultados em um dicionário em Python. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from operator import itemgetter

jogadores = {
    "jogador1": randint(0, 10),
    "jogador2": randint(0, 10),
    "jogador3": randint(0, 10),
    "jogador4": randint(0,10)
}

for k, v in jogadores.items():
    print(f"Jogador {k} tirou {v} no dado")
print()


rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print("   =-RANKING-=")

for i, values in enumerate(rank, 1):
    print(f"{i}° lugar: {values[0]} com {values[1]} pontos")