
def ficha(j="<desconhecido>", g=0):
    print(f"O jogador {j} fez {g} gol(s) no campeonato")


jogador = str(input("Nome do Jogador: ")).capitalize()
gols_feito = str(input("Número de gols: "))

if jogador == "":
    ficha(g = gols_feito)
else:
    ficha(jogador, gols_feito)

if gols_feito == "" or gols_feito.isalpha():
    gols_feito = 0

'''
if gols_feito.isnumeric():
    gols_feito = int(gols_feito)
else:
    gols_feito = 0
'''