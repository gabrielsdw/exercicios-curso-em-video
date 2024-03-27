"""Exercício Python 044: Elabore um programa que calcule
 o valor a ser pago por um produto, considerando o seu preço
 normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

precoNormalProduto = float(input("Digite o preço normal do produto: "))
condicaoDePagamento = int(input(
                                "(1) dinheiro/cheque: 10% desc\n"
                                "(2) à vista no cartão 5% desc\n"
                                "(3) em até 2x no cartão preco formal\n"
                                "(4) 3x ou mais no cartao: 20% de juros\n"
                                "Escolha uma opção de pagamento:"))



if condicaoDePagamento == 1:
    valorFinal = precoNormalProduto - (precoNormalProduto/100)*10
elif condicaoDePagamento == 2:
    valorFinal = precoNormalProduto - (precoNormalProduto/100)*5
elif condicaoDePagamento == 3:
    valorFinal = precoNormalProduto
elif condicaoDePagamento == 4:
    valorFinal = precoNormalProduto + (precoNormalProduto/100)*20
else:
    print("Opção Inválida")

print(f"O valor final é de R${valorFinal}")
