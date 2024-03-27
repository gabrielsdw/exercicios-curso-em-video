"""
Exercício Python 090: Faça um programa que
leia nome e média de um aluno, guardando
também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
dicionario = {
    "nome": input("Digite o nome do aluno: "),
    "media": float(input("Digite a média do aluno: ")),
}

if dicionario["media"] >= 7:
    dicionario["situacao"] = "Aprovado"
elif dicionario["media"] >= 5 and dicionario["media"] < 7:
    dicionario["situacao"] = "Recuperação"
else:
    dicionario["situacao"] = "Reprovado"

for k, v in dicionario.items():
    print(f"{k} = {v}")