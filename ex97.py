"""
Exercício Python 097: Faça um programa que
tenha uma função chamada escreva(), que receba
um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável.

Ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~
"""

def escreva(txt: str):

    print("~"*(len(txt)+20))
    print(f"{txt}".title().strip().center(len(txt)+20))
    print("~" * (len(txt) + 20))

escreva("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")