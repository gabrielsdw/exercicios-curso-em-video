"""
Exercício Python 083: Crie um programa onde
o usuário digite uma expressão qualquer que
use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses
abertos e fechados na ordem correta.
"""

expressao = str(input("Digite uma expressão matemática: "))

if expressao.count("(") == expressao.count(")") and expressao[0] != ")":
    print("Expressão válida!")
else:
    print("Expressão inválida!")