"""
Exercício Python 109: Modifique
as funções que foram criadas
no desafio 107 para que elas
aceitem um parâmetro a mais,
informando se o valor retornado
por elas vai ser ou não formatado
pela função moeda(), desenvolvida
no desafio 108.
"""

from ex109 import moeda
valor = float(input("Digite o valor: R$"))
porcentagem = float(input("Digite a porcentagem: %"))
print(f"Função aumentar: {moeda.aumentar(valor, porcentagem, formatacao=True)}\n"
      f"Função diminuir: {moeda.diminuir(valor, porcentagem, formatacao=True)}\n"
      f"Função dobro: {moeda.dobro(valor, formatacao=True)}\n"
      f"Função metade: {moeda.metade(valor, formatacao=True)}\n"
      f"Função moeda: {moeda.moeda(valor, moeda='$')}")