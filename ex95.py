"""
Exercício Python 095: Aprimore o desafio 93
para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
"""

dadosJogador = dict()
listaJogadores = list()
gols = list()

while True:
    dadosJogador["nome"] = str(input("Digite o nome do jogador: "))
    dadosJogador["PartidasJogadas"] = int(input("Quantas partidas ele jogou? "))
    dadosJogador["TotalGols"] = 0

    i = 0
    while i < dadosJogador["PartidasJogadas"]:
        gol = int(input(f"Quantos gols ele fez na {i+1}° Partida: "))
        gols.append(gol)
        dadosJogador["TotalGols"] += gol
        i += 1

    dadosJogador["gols"] = gols[:]
    listaJogadores.append(dadosJogador.copy())
    dadosJogador.clear()
    gols.clear()

    continuar = input("Deseja continuar? [S/N]: ").strip().upper()[0]

    if continuar == "N":
        print("-="*30)
        print("cod | nome | gols | total")
        print("-=" * 30)
        for i in range(len(listaJogadores)):
            print(f"{i} | {listaJogadores[i]['nome']} | {listaJogadores[i]['gols']} | {listaJogadores[i]['TotalGols']}")
        break

while True:

    pgt = int(input("Mostrar dados de qual jogador? (999 para parar): "))

    if pgt == 999:
        print("Programa Finalizado!")
        break
    else:
        if pgt >= len(listaJogadores):
            print("Esse jogador não existe!")
        else:
            print(f'LEVANTEMENTO DE DADOS DO JOGADOR {listaJogadores[pgt]["nome"]}')
            for k, v in enumerate(listaJogadores[pgt]["gols"], 1):
                print(f"   => Na partida {k} ele fez {v} gols ")