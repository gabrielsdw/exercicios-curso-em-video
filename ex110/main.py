"""
Exercício Python 110: Adicione
o módulo moeda.py criado nos
desafios anteriores, uma função
chamada resumo(), que na tela
algumas informações geradas
pelas funções que já temos no
módulo criado até aqui.
"""

from ex110 import moeda

valor = float(input("Digite o valor: R$"))
moeda.resumo(valor, 10, 5)