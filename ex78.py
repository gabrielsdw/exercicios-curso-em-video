"""
Exercício Python 078: Faça um programa que
leia 5 valores numéricos e guarde-os em
lista. No final, mostre qual foi o maior e
o menor valor digitado e as suas respectivas posições na lista.
"""

numeros = list()
maior = menor = 0
posicoesMenorNumero = list()
posicoesMaiorNumero = list()

for i in range(1, 6):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    if i == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero


for k, v in enumerate(numeros):
    if v == maior:
        posicoesMaiorNumero.append(k+1)
    if v == menor:
        posicoesMenorNumero.append(k+1)


print(f"\nO maior {maior} o menor {menor}")

print(f"Posições do maior número: {posicoesMaiorNumero}")
print(f"Posições do menor número: {posicoesMenorNumero}")


