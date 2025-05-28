
# crie um programa onde 4 jogadores tenham resultados aleatórios
# guarde esses resultados em um dicionário
# no final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

ranking = [] #{}

for k,v in jogo.items():
    print(f"{k} tirou {v}")
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #itemgetter 0 é as key e 1 as values 
# depois que faz o sorted o dicionario vira lista com os keys e valeus dentro de tuplas
# com isso consigo usar o enumetare no for 
# [('jogador1', 4), ('jogador2', 2), ('jogador4', 2), ('jogador3', 1)]
# assim ranking tem que ser tratado como uma lista 

# print(ranking)
print("-=" * 30)
print("Ranking dos jogadores")
for i, v in enumerate(ranking):
    print(f"{i + 1}º lugar: {v[0]} com {v[1]}")
    sleep(1)