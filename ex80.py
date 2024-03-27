"""
Exercício Python 080: Crie um programa
onde o usuário possa digitar cinco valores
numéricos e cadastre-os em uma lista, já na
posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""
listaNumeros = list()

for c in range(1, 6):
    numero = int(input("Digite um número: "))
    if c == 1 or numero > listaNumeros[-1]:
        listaNumeros.append(numero)
    else:
        i = 0
        while i < len(listaNumeros):
            if numero <= listaNumeros[i]:
                listaNumeros.insert(i, numero)
                break
            i += 1
print(listaNumeros)
