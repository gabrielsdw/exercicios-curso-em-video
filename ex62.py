"""
Exercício Python 062: Melhore o DESAFIO 061,
perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando
ele disser que quer mostrar 0 termos.
"""

primeiroTermo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo = primeiroTermo
j = 1
termos = 0

while True:
    if j == 1:
        i = 0
        while i < 10:
            print(termo, end=" ")
            termo += razao
            termos = i
            i += 1

    vezes = int(input("\nDeseja ver mais quantas vezes? "))
    if vezes != 0:
        c = 0
        while c < vezes:
            print(termo, end=" ")
            termo += razao
            termos += 1
            c += 1
    else:
        print("Programa Finalizado!")
        print(f"Você viu {termos+1} termos desta PA.")
        break
    j += 1
