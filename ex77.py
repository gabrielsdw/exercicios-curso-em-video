"""
Exercício Python 077: Crie um programa
que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve
mostrar, para cada palavra, quais são as suas vogais.
"""

tupla = ('cachorro', 'gato', 'cobra', 'elefante', 'paralelepipedo')
vogais = ("a", "e", "i", "o", "u")

for palavra in tupla:
    print(f"\nVogais da palavra {palavra}: ", end="")
    for letra in palavra:
        if letra in vogais:
            print(letra, end=" ")