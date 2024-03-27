from math import hypot
cmpCatetoOposto = float(input("Digite o comprimento do cateto oposto: "))
cmpCatetoAdjacente = float(input("Digite o comprimento do cateto adjacente: "))
cmpHipotenusa = hypot(cmpCatetoOposto, cmpCatetoAdjacente)
print(f"A hipotenusa vai medir {cmpHipotenusa:.2f}")