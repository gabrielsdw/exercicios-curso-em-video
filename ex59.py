"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
print("Digite 0 para ver o menu ")

while True:
    opcao = int(input("Escolha uma opção: "))
    if opcao == 0:
        print(f" [ 1 ] somar\n"
              "[ 2 ] multiplicar\n"
              "[ 3 ] maior\n"
              "[ 4 ] novos números\n"
              "[ 5 ] sair do programa")

    elif opcao == 1:
        print(f"{numero1} + {numero2} = {numero1+numero2}")
    elif opcao == 2:
        print(f"{numero1} x {numero2} = {numero1*numero2}")
    elif opcao == 3:
        if numero1 > numero2:
            print(f"O maior número é {numero1}")
        else:
            print(f"O maior número é {numero2}")
    elif opcao == 4:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

    elif opcao == 5:
        break
    else:
        print("Opção inválida!")
