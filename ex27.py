nomeCompleto = str(input("Digite seu nome Completo: ")).strip().title()
primeiroNome = nomeCompleto.split()[0]
ultimoNome = nomeCompleto.split()[-1]
print(f"Seu primeiro nome é: {primeiroNome}")
print(f"Seu último nome é: {ultimoNome}")
print(nomeCompleto)