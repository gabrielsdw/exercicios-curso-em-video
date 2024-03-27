altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))
area = altura*largura
quantidadeDeTinta = area/2
print(f"A parede tem a dimensão de {largura}x{altura} e sua área é de {area} m².")
print(f"Para pintar esta parede você precisará de {quantidadeDeTinta} litros de tinta.")