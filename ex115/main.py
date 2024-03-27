from ex115.funções import interface
from ex115.funções import arquivo

if not arquivo.verificaArquivo("nomes.txt"):
    arquivo.criaArquivo("nomes.txt")

while True:
    resp = interface.menu(["Ver Pessoas Cadastradas", "Cadastrar Nova Pessoa", "Sair"])
    if resp == 1:
        arquivo.lerArquivo("nomes.txt")
    elif resp == 2:
        nome = input("Digite o nome a ser cadastrado: ")
        idade = interface.leiaInt("Digite a idade a ser cadastrada: ")
        arquivo.cadastrarPessoa(nome, idade)
    elif resp == 3:
        interface.cabecalho("PROGRAMA FINALIZADO!")
        break
    else:
        print("Opção inválida")