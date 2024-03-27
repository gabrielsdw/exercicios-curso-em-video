distanciaEmKM = float(input("Digite a distância da viagem por KM: "))
if distanciaEmKM <= 200:
    precoPorKM = distanciaEmKM*0.5
    valorViagem = precoPorKM
else:
    precoPorKm = distanciaEmKM*0.45
    valorViagem = precoPorKm

print(f"O valor total da viagem ficou R${valorViagem:.2f}")