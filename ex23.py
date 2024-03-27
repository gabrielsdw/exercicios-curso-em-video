numero = int(input("Digite um número de 1 até 9999: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print("Unidades:", unidade)
print("Dezenas:", dezena)
print("Centenas:", centena)
print("Milhares:", milhar)
