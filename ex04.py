dado = input("Digite algo: ")
print(f"O tipo primitivo deste valor é {type(dado)}")
print("Tem espaços? ", dado.isspace())
print("É númerico? ", dado.isnumeric())
print("É alfabético? ", dado.isalpha())
print("É alfanumérico? ", dado.isalnum())
print("Está em letras maiúsculas? ", dado.isupper())
print("Está em letras minúsculas? ", dado.islower())
print("Está capitalizada? ", dado.istitle())