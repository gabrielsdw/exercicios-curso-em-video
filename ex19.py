from random import choice
nomesAlunos = []
for i in range(0, 4):
    aluno = input(f"Digite o nome do {i+1}° aluno: ")
    nomesAlunos.append(aluno)
alunoEscolhido = choice(nomesAlunos)
print(f"O aluno escolhido foi {alunoEscolhido}")