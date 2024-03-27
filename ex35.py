a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))
if a + b > c and b + c > a and a + c > b:
    print("Essas medidas podem formar um triângulo")
else:
    print("Essas medidas NÃO podem formar um triângulo")