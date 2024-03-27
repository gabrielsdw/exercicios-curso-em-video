from ex115.funções.interface import cabecalho
import datetime


def verificaArquivo(nome):
    try:
        arquivo = open(nome, "r")
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArquivo(nome):
    try:
        arquivo = open(nome, "wt+")
        arquivo.close()
    except:
        print("Erro ao criar arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    with open(nome, "r") as arquivo:
        f = arquivo.readlines()
    if len(f) > 0:
        cabecalho("NOVA PESSOA CADASTRADA")

        lista = list()
        for k in f:
            lista.append(k.split(";"))
            for c in range(len(lista)):
                lista[c][1] = lista[c][1].replace("\n", "")

        for c in range(len(lista)):
            print(f"{c + 1} - {lista[c][0]}    {lista[c][1]} anos       {lista[c][2]}")
    else:
        print("Não há pessoas cadastradas!")




def cadastrarPessoa(nome, idade):
    data = datetime.date.today()
    with open("nomes.txt", "a") as arquivo:
        f = arquivo.write(f"{nome};{idade};{data}\n")

    print(f"{nome} foi cadastrado(a) com sucesso!")