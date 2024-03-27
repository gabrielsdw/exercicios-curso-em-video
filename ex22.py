nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome em letras maiúsculas é:", nome.upper())
print("Seu nome em letras minúsculas é:", nome.lower())
print(f"Seu nome completo tem {len(nome)-nome.count(' ')} letras ")
primeiroNome = nome.split(" ")[0]
print(f"Seu primeiro nome é", primeiroNome, "e ele contém", len(primeiroNome), "letras")
