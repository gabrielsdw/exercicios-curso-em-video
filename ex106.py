"""
Exercício Python 106: Faça um mini-sistema que
utilize o Interactive Help do Python. O usuário
vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM',
o programa se encerrará. Importante: use cores.
"""


def main():
    print("~"*40)
    print("Sistema de Ajuda".center(40))
    print("~"*40)

    while True:
        lib = input("Digite a biblioteca/função a ser pesquisada: ").strip().lower()
        print()
        if lib == "fim":
            print("PROGRAMA FINALIZADO!")
            break
        else:
            print(help(lib))


main()