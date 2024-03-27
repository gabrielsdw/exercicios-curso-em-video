precoProduto = float(input("Digite o preço do produto: "))
valorDesconto = (precoProduto*5)/100
precoProdutoComDesconto = precoProduto-valorDesconto
print(f"O preço do produto com 5% de desconto é de R${precoProdutoComDesconto}")