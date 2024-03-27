"""
Exercício Python 113: Reescreva
a função leiaInt() que fizemos no desafio 104,
 incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e
crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(txt=None):
    while True:
        try:
            numero = int(input(txt))
        except (ValueError, TypeError):
            print("ERRO! Digite um número inteiro válido!")
            continue
        except KeyboardInterrupt:
            print("\nERRO! O usuário decidiu não enviar os dados!")
            return 0
        else:
            return numero


def leiaFloat(txt=None):
    while True:
        try:
            numero = float(input(txt))
        except(ValueError, TypeError):
            print("Erro! Digite um número flutuante válido!")
            continue
        except(KeyboardInterrupt):
            print("\nErro! O usuário decidiu não enviar os dados!")
            return 0
        else:
            return numero


numeroInteiro = leiaInt("Digite um número inteiro: ")
numeroReal = leiaFloat("Digite um número real: ")

print(f"O número inteiro digitado foi {numeroInteiro} e o número real {numeroReal}")