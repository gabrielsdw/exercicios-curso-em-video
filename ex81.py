"""
Exercício Python 081: Crie um programa que vai ler vários
números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []

while (True):
    numero = int(input("Digite um número: "))
    lista.append(numero)
    continuar = input("Deseja continuar? (S/N): ").strip().lower()[0]
    if continuar == "n":
        break
print(f"{len(lista)} números foram digitados.")
lista.sort()
print(f"Os valores em forma decrescente: {lista[::-1]}")

#lista.sort(reverse=True)
#print(f"Os valores em forma decrescente: {lista}")

if 5 in lista:
    print("5 está na lista")
else:
    print("5 não está na lista")