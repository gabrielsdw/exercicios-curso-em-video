"""
Exercício Python 112: Dentro do
pacote utilidadesCeV que criamos
no desafio 111, temos um módulo
chamado dado. Crie uma função
chamada leiaDinheiro() que seja
capaz de funcionar como a função
input(), mas com uma validação
de dados para aceitar apenas valores
que seja monetários.
"""

from ex112.utilidadesCEV import moedas, dados

valor = dados.leiaDinheiro("Digite um valor: ")
moedas.resumo(valor, 10, 5)