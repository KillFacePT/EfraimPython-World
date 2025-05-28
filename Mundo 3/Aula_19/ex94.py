
# crie um programa que leia nome, sexo e idade de várias pessoas
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista
# no final mostre:
# a) qunatas pessoas foram cadastradas
# b) a média de idade do grupo
# c) uma lista com todas as mulheres
# d) uma lista com todas as pessoas com idade acima da média

pessoa = {}
lista_pessoas = []
lista_mulheres = []
lista_idade_acima_media = []
quant_pessoas = 0
soma_idade = 0

while True:

    pessoa['nome'] = str(input("Nome: ")).capitalize()
    pessoa['sexo'] = str(input("Sexo [M/F]: ")).lower().strip()[0]
    
    while pessoa['sexo'] not in "fm":
        pessoa['sexo'] = str(input("Digite apanas 'M' ou 'F' [M/F]: ")).lower().strip()[0]

    pessoa['idade'] = int(input("Idade: "))

    soma_idade +=  pessoa['idade']

    sair = ' ' # while sair not in "s":
    sair = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]

    while sair not in "sn":
        sair = str(input("Digite 'S' ou 'N' para continuar [S/N]: ")).lower().strip()[0]

    lista_pessoas.append(pessoa.copy())
  
    if pessoa['sexo'] == 'f':
        lista_mulheres.append(pessoa['nome'])

    quant_pessoas += 1

    if sair in "n":
        break

media = int(soma_idade / quant_pessoas)

for p in lista_pessoas:
      if p['idade'] > media:
          lista_idade_acima_media.append(p['nome'])

print(" ")
print(lista_pessoas)
print(" ")
print(f"Foram cadastradas no total de {quant_pessoas} pessoas.") #len(lista_pessoas)
print(f"A Média de idade do grupo é: {media}")
print(f"A Lista de mulhers: {lista_mulheres}")
print(f"Lista de pessoas com idade acima da média: {lista_idade_acima_media}")