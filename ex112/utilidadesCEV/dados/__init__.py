def leiaDinheiro(texto):
    while True:
        valor = str(input(texto)).strip().replace(",", ".")

        if valor.replace(".", "").isnumeric():
            return float(valor)
        else:
            print(f"ERRO! '{valor}' não é um valor numérico ")