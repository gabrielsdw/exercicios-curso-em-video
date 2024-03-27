from math import sin, cos, tan, radians
angulo = float(input("Digite o valor de um ângulo qualquer: "))


print(f"Cosseno: {cos(radians(angulo)):.2f} \n"
      f"Seno: {sin(radians(angulo)):.2f} \n"
      f"Tangente: {tan(radians(angulo)):.2f}")