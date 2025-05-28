
# crie um programa que leia o nome de uma cidade 
# e diga se ela começa ou não com o nome "santo"

cidade = str(input("Digite o nome de sua cidade: ")).strip(" ").lower()


print(cidade[0:5] == "santo")
print(cidade.startswith("santo"))