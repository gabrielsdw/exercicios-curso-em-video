"""
Exercício Python 079: Crie um programa onde
o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão
exibidos todos os valores únicos digitados, em ordem crescente.
"""

listaNumero = list()

continuar = "s"
while continuar in "s":
    numero = int(input("Digite um número: "))
    if numero not in listaNumero:
        listaNumero.append(numero)
        print("Valor Adicionado Com Sucesso!")
    else:
        print("Esse número já existe na lista!")
    continuar = input("Deseja continuar? (S/N)").strip().lower()[0]

listaNumero.sort()
print(f"Os números ordenados são {listaNumero}")