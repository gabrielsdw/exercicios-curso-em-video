from random import randint

numeroPensado = randint(0, 5)
numeroDigitado = int(input("Tente adivinhar o número de 1 a 5 em que a máquina pensou: "))

if numeroDigitado == numeroPensado:
    print(f"Você acertou!!! O número em que pensei foi {numeroPensado}")
else:
    print(f"Você errou!!! O número em que pensei foi {numeroPensado}")
