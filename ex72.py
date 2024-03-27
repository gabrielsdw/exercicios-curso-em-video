"""
Exercício Python 072: Crie um programa que
tenha uma dupla totalmente preenchida com uma
contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.
"""

extenso = ("Zero", "um", "dois", "três", "Quatro",
           "Cinco", "Seis", "Sete", "Oito",
           "Nove", "Dez", "Onze", "Doze",
           "Treze", "Quatorze", "Quinze",
           "Dezesseis", "Dezessete", "Dezoito",
           "Dezenove", "Vinte")

while True:
    numero = int(input("Digite um número ENTRE 0 E 20: "))
    if numero >= 0 and numero <= 20:
        print(f"O extenso de {numero} é {extenso[numero]}")
        break
    else:
        continue