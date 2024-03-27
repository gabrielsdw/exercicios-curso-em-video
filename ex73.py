"""
Exercício Python 073: Crie uma tupla preenchida
com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

times = ("Flamengo","Santos","Palmeiras","Gremio",
             "Atletico Paranaense", "São Paulo","Internacional",
             "Conrithians","Fortaleza","Goias","Bahia","Vasco",
             "Atletico Mineiro","Fluminense","Botafogo","Ceará",
             "Cruzeiro","CSA","Chapecoense","Avaí")

print("Os 5 primeiros times são:")
print(times[0:5])

print("Os 4 últimos colocados são:")
print(times[-4:])

print("Os times em Ordem Alfabética:")
print(sorted(times))

print(f"O time da chapecoense está na posição {times.index('Chapecoense')+1}")