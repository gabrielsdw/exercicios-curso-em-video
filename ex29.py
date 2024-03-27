velocidadeDoCarro = float(input("Em qual velocidade você andou com o carro? "))

if velocidadeDoCarro > 80:
    valorDaMulta = (velocidadeDoCarro-80) * 7
    print("VOCÊ FOI MULTADO!!!")
    print(f"O valor da multa que você recebeu é de R${valorDaMulta:.2f}")
else:
    print("PARABÉNS, VOCÊ NÃO EXCEDEU O LIMITE DE VELOCIDADE!!!")