"""
Exercício Python 108: Adapte
o código do desafio #107, criando
uma função adicional chamada moeda()
que consiga mostrar os números como
um valor monetário formatado.
"""

from ex108 import moeda
valor = float(input("Digite o valor: R$"))
porcentagem = float(input("Digite a porcentagem: %"))
print(f"Função aumentar: {moeda.moeda(moeda.aumentar(valor, porcentagem))}\n"
      f"Função diminuir: {moeda.moeda(moeda.diminuir(valor, porcentagem))}\n"
      f"Função dobro: {moeda.moeda(moeda.dobro(valor))}\n"
      f"Função metade: {moeda.moeda(moeda.metade(valor))}\n"
      f"Função moeda: {moeda.moeda(valor, moeda='$')}")