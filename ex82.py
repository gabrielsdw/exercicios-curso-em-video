"""
Exercício Python 082: Crie um programa que vai
ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que
vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final,
mostre o conteúdo das três listas geradas.
"""

lista = list()

while (True):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    continuar = int(input("Digite 0 para Parar e 1 Para Continuar: "))
    if continuar == 0:
        break

listaPares = [x for x in lista if x % 2 == 0]
listaImpares = [x for x in lista if x % 2 == 1]

print(f"Os valores digitados foram: {lista}")
print(f"Os valores pares digitados foram: {listaPares}")
print(f"Os valores ímpares digitados foram: {listaImpares}")