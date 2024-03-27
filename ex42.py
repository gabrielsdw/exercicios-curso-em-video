"""Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
   acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""



a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

if a + b > c and b + c > a and a + c > b:
    if a == b and a == c:
        print("EQUILÁTERO")
    elif a == b and a != c or a == c and a != b:
        print("ISÓSCELES")
    else:
        print("ESCALENO")

else:
    print("Essas medidas NÃO podem formar um triângulo")