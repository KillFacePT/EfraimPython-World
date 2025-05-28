
# faça um programa que tenha a função chamada ficha() que receba dois parâmetros opcionais
# o nome de um jogador e quantos gols ele marcou 
# o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente



jogador = str(input("Nome do Jogador: ")).capitalize()
gols_feito = str(input("Número de gols: "))


def ficha(j, g):

    if j == "":
        j = "<desconhecido>"

    if g == "" or g.isalpha():
        g = 0

    return f"O jogador {j} fez {g} gol(s) no campeonato"


print(ficha(jogador, gols_feito))