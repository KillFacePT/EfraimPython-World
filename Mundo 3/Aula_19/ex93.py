
# crie um programa que gerencia o aproveitamento de um jogador de futebol
# o programa vai ler o nome do jogador e quantas partidas ele jogou.
# depois vai ler a quantidades de gols feitos em cada partida.
# no final, tudo isso será guardade em um dicionário, incluindo o total de gols feitos durante o campeonato

jogador = {}
gols = []

jogador['nome'] = str(input("Jogador: ")).capitalize()

partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

print("-=" * 30)


total_gols = 0
for g in range(partidas):
    
    gols_marcados = int(input(f"Quantos gols na partida {g + 1}: "))
    gols.append(gols_marcados)

    total_gols += gols_marcados

jogador['gols'] = gols
jogador['total Gols'] = total_gols

print("-=" * 30)
print(jogador)
print("-=" * 30)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")

print("-=" * 30)

print(f"O jogador {jogador['nome']} jogou {partidas} partidas")

for i, gl in enumerate(gols):
    print(f"Na partida {i + 1}, fez {gl}")
    
print(f"Foi um total de {total_gols} gols.")    
