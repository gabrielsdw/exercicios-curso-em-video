"""
Exercício Python 107: Crie um módulo chamado
moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo
e use algumas dessas funções.
"""

from ex107 import moeda

valor = float(input("Digite o valor: R$"))
porcentagem = float(input("Digite a porcentagem: %"))
print(f"Função aumentar: {moeda.aumentar(valor, porcentagem)}\n"
      f"Função diminuir: {moeda.diminuir(valor, porcentagem)}\n"
      f"Função dobro: {moeda.dobro(valor)}\n"
      f"Função metade: {moeda.metade(valor)}")