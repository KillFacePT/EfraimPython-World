
# crie um programa que tenha uma Tupla única com nomes de produtos e seus respectivos preçõs, na sequência
# no final, mostre uma listagem de preços, organizando os dados em forma tabular.

                          #1            #3             #5             #7                #9
listagem = ("Chocolate", 5.35, "Cafe", 3.14, "Carne", 90.00, "Suco", 6.87, "Brocolis", 1.29)

print("-" * 40)
print(f"{"LISTAGEM DE PREÇOS":^40}")
print("-" * 40)

for i in range(0, len(listagem), 2): # O step está em dois por causa dos preços
    print(f"{listagem[i]:.<30}R$ {listagem[i + 1]:>7.2f}") # primeiro index = 0, preço do index 0 é index + 1 = 0 + 1 e assim por diante o proximo preco esta no index 3 
                                                    # por isso do step de dois em dois

print("-" * 40)

#:.<30 alinhado a esquerda os produtos(o ponto vai completar os espaços vazios)

for i in range(0, len(listagem)): 
    if i % 2 == 0: # se i que "i" seria a posição
        print(f"{listagem[i]:.<30}", end="")
    else:
        print(f"R${listagem[i]:>7.2f}")
    
# :> 7.2f alinhando a direita e o ".2f" é as casas decimais