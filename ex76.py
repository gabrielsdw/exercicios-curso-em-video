"""
Exercício Python 076: Crie um programa que
tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços,
organizando os dados em forma tabular.
"""

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

c = 0
for i in range(1, len(produtos), 2):
    print(f"{produtos[c]} R${produtos[i]}")
    c += 2


