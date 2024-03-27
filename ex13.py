salarioFuncionario = float(input("Digite o salário do funcionário: "))
novoSalarioFuncionario = salarioFuncionario + ((salarioFuncionario*15)/100)
print(f"O salário do funcionário de R${salarioFuncionario} após o reajuste de \n"
      f"15% é de {novoSalarioFuncionario:.2f}")