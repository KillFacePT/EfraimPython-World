
# crie um programa que leia o nome e o preço de vários produtos
# o programa deverá perguntar se o usuário vai continuar
# no final mostre 
# a) qual é o total gasto na compra
# b) quantos produtos custam mais de R$ 1000
# c) qual é o nome do produto mais barato
print("=" * 40)
print(f"{"LOJÃO BARATEZA":^40}")
print("=" * 40)

gasto = 0
mais1000 = 0
contador = 0
valor_barato = 0
nome_prod_barato = " "

#compras = {}

while True:

    produto = str(input("Produto: "))
    preco = float(input("Preço R$: "))
    
    gasto += preco
    contador +=1
    
    
    if contador == 1: # or preco < valor_barato, posso usar o "OR" e remover o else
        valor_barato = preco # primeiro valor digitado vira o valor caro e barato ao mesmo tempo
        nome_prod_barato = produto # primeiro produto digitado vira o produco mais barato e mais caro ao mesmo tempo
    else:
        if preco < valor_barato: # se o preco do proximo produto for mais barato que o "valor_barato" esse novo preço vai ser o mais barato e o nome do produto também
            valor_barato = preco 
            nome_prod_barato = produto

    
    if preco > 1000:
        mais1000 += 1


    continuar = " "
    while continuar not in "sn":
        continuar = str(input("Deseja adicionar mais produtos? [S/N] ")).strip().lower()[0] # se escrever sim/não vai apenas pegar a primeira letra

    #compras[produto] = preco # adiciona key e value na lista key é produto, value é o preço
    
    if continuar == "n":
        break

# barato = min(compras.values())
# produto_barato = sorted(compras.items(), key = lambda x: x[1]) # sorted() ordena pelo value, então se o value for o mais barato consegue o produto mais barato 

print(f"Valor total da compra R$: {gasto:.2f}")
print(f"Você comprou {mais1000} produto(s) que custam mais de R$1.000,00 Reais")
# print(f"O produto mais barato foi {produto_barato[0][0]} que custa R$:{barato}")
print(f"O produto mais barato foi {nome_prod_barato} que custa R$:{valor_barato:.2f}")

'''
compras = {}

while True:
    compras[produto] = preco

    break

barato = sorted(compras.keys())

print(f"O produto mais barato foi {} que custa R$:{barato}")
'''