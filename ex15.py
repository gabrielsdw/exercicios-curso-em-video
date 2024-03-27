quantidadeDeKmPercorrido = float(input("Quantos KM você percorreu? "))
quantidadeDeDiasAlugado = float(input("Quantos dias o carro foi alugado? "))
custoPorKM = quantidadeDeKmPercorrido * 0.15
custoPorDia = quantidadeDeDiasAlugado * 60
custoTotal = custoPorKM + custoPorDia
print(f"O total a pagar é de R${custoTotal}")