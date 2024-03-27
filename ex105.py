"""
Exercício Python 105: Faça um programa que tenha
uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as
seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
"""

def notas(*notas, situacao=None):
    """
    <<
    Função que devolve dados de uma turma.
    >>
    :param notas: notas dos alunos
    :param situacao: (Opcional) incluir a situação da sala ou não
    :return: retorna um dicionário com as informações da turma
    """

    dicionarioNotas = {
        "Total": len(notas),
        "maiorNota": max(notas),
        "menorNota": min(notas),
        "mediaDaTurma": sum(notas) / len(notas)
    }

    if situacao:
        if dicionarioNotas["mediaDaTurma"] >= 7:
            dicionarioNotas["situação"] = "Boa"
        elif dicionarioNotas["mediaDaTurma"] >= 5:
            dicionarioNotas["situação"] = "Média"
        else:
            dicionarioNotas["situação"] = "Ruim"

    return dicionarioNotas