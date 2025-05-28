
# crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol
# na ordem de colocação. depois mostre:
# a) apenas os 5 primeiros colocados
# b) os últimos 4 colocados da tabela
# c) uma lista com os times em ordem alfabética
# d) em que posição na tabela está o time da capecoense 

brasileirao = (
    "Corinthians",
    "Palmeiras",
    "Grêmio",
    "Santos",
    "Cruzeiro",
    "Flamengo",
    "Vasco da Gama",
    "Chapecoense",
    "Atlético Mineiro",
    "Botafogo",
    "Atlético Paranaense",
    "Bahia",
    "São Paulo",
    "Fluminense",
    "Sport Recife",
    "Vitória",
    "Coritiba",
    "Avaí",
    "Ponte Preta",
    "Atlético Goianiense"
)

print(brasileirao[0:5])
print("-=" * 30)
print(brasileirao[16:]) # ou [-4::]
print("-=" * 30)
print(sorted(brasileirao))
print("-=" * 30)
print(f"O chapecoense está na {brasileirao.index("Chapecoense") + 1}ª posição")