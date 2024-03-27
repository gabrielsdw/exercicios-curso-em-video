def leiaInt(txt=None):
    while True:
        try:
            numero = int(input(txt))
        except (ValueError, TypeError):
            print("ERRO! Digite um número inteiro válido!")
            continue
        except KeyboardInterrupt:
            print("\nERRO! O usuário decidiu não enviar os dados!")
            return 0
        else:
            return numero


def linha():
    print("~"*40)


def cabecalho(txt=""):
    linha()
    print(txt.center(40))
    linha()


def menu(lista:list):
    cabecalho("MENU PRINCIPAL")
    for k, v in enumerate(lista, 1):
        print(f"{k} - {v}")
    linha()
    opcao = leiaInt("Sua opção: ")
    return opcao



