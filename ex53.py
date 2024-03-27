"""
Exercício Python 053: Crie um programa que leia
uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
"""

frase = str(input("Digite uma FRASE: ")).strip().lower().split(" ")

fraseJunta = "".join(frase)

print(f"O inverso de {fraseJunta} é {fraseJunta[::-1]}")

if fraseJunta[::-1] == fraseJunta:
    print("Temos um palíndromo")
else:
    print("Não temos um palíndromo")