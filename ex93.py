"""
Exercício Python 093: Crie um programa
que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a
quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

dadosJogador = dict()

dadosJogador["nome"] = str(input("Digite o nome do jogador: "))
dadosJogador["PartidasJogadas"] = int(input("Quantas partidas ele jogou? "))

i = 0
dadosJogador["TotalGols"] = 0
gols = list()
while i < dadosJogador["PartidasJogadas"]:
    gol = int(input(f"Quantos gols ele fez na {i+1}° Partida: "))
    gols.append(gol)
    dadosJogador["TotalGols"] += gol
    i += 1
dadosJogador["gols"] = gols

print("-="*30)
print(dadosJogador)
print('-='*30)
for k, v in dadosJogador.items():
    print(f"O campo {k} tem o valor {v}")
print('-='*30)
print(f"O jogador {dadosJogador['nome']} jogou {dadosJogador['PartidasJogadas']} partidas")
for k, v in enumerate(gols, 1):
    print(f"  => Na partida {k}, ele fez {v} gols")
print(f"Foi um total de {dadosJogador['TotalGols']} gols")
print('-='*30)
