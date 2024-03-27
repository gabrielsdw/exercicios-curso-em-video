"""
Exercício Python 100: Faça um programa que
tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da
lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.
"""

def sorteia(lista:list):
    from random import randint
    for c in range(0, 5):
        lista.append(randint(-10,100))
    return lista


def somaPar(lista:list):
    #listaPares = list(filter(lambda x: x % 2 == 0, lista))
    listaPares = [x for x in lista if x % 2 == 0]
    return sum(listaPares)


lista = []
sorteia(lista)

print(f"A soma de todos os números pares de {lista} é {somaPar(lista)}")

