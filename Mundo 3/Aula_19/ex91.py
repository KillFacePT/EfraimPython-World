
# crie um programa onde 4 jogadores tenham resultados aleatórios
# guarde esses resultados em um dicionário
# no final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint

jogo = {}

print("Valores sorteaods:")

for j in range(0, 4):
    
    jogo[f'pedra{j + 1}'] = randint(1, 6)

    print(f"O jogaodr {j + 1} tirou {jogo[f'pedra{j + 1}']}")


print("Ranking dos jogadores:")
# for k, v in sorted()