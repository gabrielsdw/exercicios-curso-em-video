numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 < numero2 and numero1 < numero3:
    menorNumero = numero1
if numero2 < numero1 and numero2 < numero3:
    menorNumero = numero2
if numero3 < numero1 and numero3 < numero2:
    menorNumero = numero3
if numero1 > numero2 and numero1 > numero3:
    maiorNumero = numero1
if numero2 > numero1 and numero2 > numero3:
    maiorNumero = numero2
if numero3 > numero1 and numero3 > numero2:
    maiorNumero = numero3


print(f"O menor número é: {menorNumero}")
print(f"O maior número é: {maiorNumero}")
