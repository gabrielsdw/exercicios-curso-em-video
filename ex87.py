"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0

for j in range(0,3):
    for k in range(0,3):
        numero = int(input("Digite um número: "))
        matriz[j][k] = numero
        if numero % 2 == 0:
            soma += numero

for linha in matriz:
    print(linha)

print()
print(f"A soma de todos os valores pares digitados: {soma}")

soma = 0
for i in range(len(matriz[2])):
    soma += matriz[2][i]

print(f"A soma dos valores da terceira coluna: {soma}")
print(f"O maior valor da segunda coluna: {max(matriz[1])}")

