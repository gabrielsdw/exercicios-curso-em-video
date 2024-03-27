"""
Exercício Python 070: Crie um programa que leia
o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou
não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""
totalGastoNaCompra = 0
nomeProdutoMaisBarato = str()
precoProdutoMaisBarato = 0
produtoMaisDe1000Reais = 0

c = 0
while (True):
    nomeProduto = input("Digite o nome do produto: ")
    precoProduto = float(input("Digite o preço deste produto: R$ "))
    totalGastoNaCompra += precoProduto
    c += 1
    if c == 1 or precoProduto < precoProdutoMaisBarato:
        nomeProdutoMaisBarato = nomeProduto
        precoProdutoMaisBarato = precoProduto
    else:
        if precoProduto < precoProdutoMaisBarato:
            precoProdutoMaisBarato = precoProduto
            nomeProdutoMaisBarato = nomeProduto

    if precoProduto > 1000:
        produtoMaisDe1000Reais += 1

    opcao = " "
    while opcao not in "SN":
        opcao = input("Deseja continuar? [S/N]: ").upper().strip()[0]
    if opcao == "N":
        print(f"O total gasto na compra é de R${totalGastoNaCompra}")
        print(f"{produtoMaisDe1000Reais} produtos custam mais de R$1000")
        print(f"O nome do produto mais barato é {nomeProdutoMaisBarato} e custa R${precoProdutoMaisBarato}")
        break