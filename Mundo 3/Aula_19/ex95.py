
# aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização 
# de detalhes de aproveitamento de cada jogador 
jogadores = {}
gols = []
gol = []
time = []

while True:

    jogadores['nome'] = str(input("Jogador: ")).capitalize()

    jogadores["partidas"] = int(input(f"Quantas partidas {jogadores['nome']} jogou? "))
    gols.clear()
    total_gols = 0
    for g in range(jogadores['partidas']):
        gols_marcados = int(input(f"Quantos gols na partida {g + 1}: "))
        gols.append(gols_marcados)
        
        total_gols += gols_marcados
        
    
    jogadores['gols'] = gols[:]
    jogadores["Total Gols"] = total_gols

    time.append(jogadores.copy())

    sair = " "
    sair = str(input("Adicionar outro Jogador? [S/N]: ")).lower().strip()[0]

    while sair not in "sn":
        sair = str(input("Digite apenas 'S' ou 'N': "))

    if sair in "n":
        break

print("-=" * 20)
print(f"{"Cod"}{"Nome":>8}{"Gols":>10}{"Total":>15}")
print("-" * 40)

for i, j in enumerate(time):
    print(f"{i}{j['nome']:>10} {str(j['gols']):>12}{j['Total Gols']:>10}") # :>12 é onde o ultimo index da palavra vai parar, index 12 a direita


while True:
    print("-" * 40)
    n = int(input("Mostrar dados de qual jogador? "))
    if n == 999:
        break

    if n >= len(time):
        print(f"ERRO! não existe jogador com código {n}, tente novamente.")

    else:
        print(f"Levantamento do jogador, {time[n]['nome']}:")
        for i, g in enumerate(time[n]['gols']):
            print(f"No jogo {i + 1}, fez {g}")

print("VOLTE SEMPRE")



# print("-=" * 30)
# print("APROVEITAMENTO DE GOLS %")
# print("-=" * 30)

# for i, g in enumerate(time):
#     print(f"O {g['nome']} teve um aproveitamento de {g['aproveitamento']}%")

# print(time)