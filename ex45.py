from random import randint
print("Suas Opções:\n"
      "(0) Pedra\n"
      "(1) Papel\n"
      "(2) Tesoura\n")

opcao = int(input("Escolha sua opção: "))


itens = ("Pedra", "Papel", "Tesoura")
jogador = itens[opcao]
maquina = itens[randint(0,2)]


if jogador == "Papel" and maquina == "Tesoura" or jogador == "Pedra" and maquina == "Papel" or jogador == "Tesoura" and maquina == "Pedra":
    print(f"A máquina escolheu {maquina}")
    print(f"O jogador escolheu {jogador}")
    print("A máquina venceu!")

elif jogador == "Tesoura" and maquina == "Papel" or jogador == "Papel" and maquina == "Pedra" or jogador == "Pedra" and maquina == "Tesoura":
    print(f"A máquina escolheu {maquina}")
    print(f"O jogador escolheu {jogador}")
    print("O jogador venceu!")

else:
    print(f"A máquina escolheu {maquina}")
    print(f"O jogador escolheu {jogador}")
    print("EMPATE!")






