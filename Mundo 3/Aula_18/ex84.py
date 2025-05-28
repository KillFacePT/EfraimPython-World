
# faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. no final mostre:
# a) quantas pessoas foram cadastradas
# b) uma listagem com as pessoas mais pesadas
# c) uma listagem com as pessoas mais leves

nome_peso = []
dados = []
maior, menor = 0, 0

while True:

    dados.append(str(input("Nome: ")))
    dados.append(float(input("Digite o peso: ")))
    
    if len(nome_peso) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]

        if dados[1] < menor:
            menor = dados[1]

    nome_peso.append(dados[:])
    dados.clear()

    continuar = " "
    while continuar not in "sn":
       continuar = str(input("Deseja continuar? [S/N] ")).lower()[0]

    if continuar in "n":
        break


print(f"Foram cadastradas {len(nome_peso)} pessoas")

print(f"O maior peso foi de {maior}Kg. Peso de ", end="")
for p in nome_peso:
    if p[1] == maior: # se o peso for maior. p[1] significa posição do peso de cada pessoa. p é o index para cada lista e [1] é o index do peso 
        print(f"[{p[0]}]", end="")
print()

print(f"O menor peso foi de {menor}Kg. Peso de ", end="")
for p in nome_peso:
    if p[1] == menor: 
        print(f"[{p[0]}]", end="")
print()

for nome, peso in nome_peso: # o primeiro valor vai para o nome e o segundo para o peso 
    if peso == maior:
        print(f"{nome}")