from random import shuffle
listaNomeAlunos = list()
for i in range(0, 4):
    nomeAluno = input(f"Digite o nome do {i + 1}° aluno: ")
    listaNomeAlunos.append(nomeAluno)
shuffle(listaNomeAlunos)
print(f"A ordem de apresentação será {listaNomeAlunos}")