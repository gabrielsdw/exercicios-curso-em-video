'''Escreva um programa para aprovar o empréstimo bancário para a compra de
uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos
 ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo
será negado.'''

valorCasa = float(input("Digite o valor da casa: R$"))
salarioComprador = float(input("Digite o salário do comprador: R$"))
quantidadeAnosParcelados = int(input("Digite em quantos anos você quer parcelar: "))

prestacao = (valorCasa / quantidadeAnosParcelados) / 12
salarioCompradorPercentualMinimo = (salarioComprador/100)*30

print(f"Para pagar uma casa de R${valorCasa} em {quantidadeAnosParcelados} anos\n"
        f"é necessário R${prestacao:.2f} por mês")

if salarioCompradorPercentualMinimo <= prestacao:
    print("Empréstimo negado!")
else:
    print("Empréstimo aceito!")