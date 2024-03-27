salarioAtual = float(input("Digite o seu salário atual: "))
if salarioAtual > 1250:
    reajuste = 10
    salarioNovo = salarioAtual + (salarioAtual/100)*reajuste
else:
    reajuste = 15
    salarioNovo = salarioAtual + (salarioAtual/100)*reajuste

print(f"O seu salário com o reajuste de {reajuste}% agora é de R${salarioNovo}")