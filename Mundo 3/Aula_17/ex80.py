
# crie um programa onde o usuário possa digitar 5 valores númericos e cadastre-os em uma lista
# ja na posição correta de inserção (sem usar o sort())
# no final mostre a lista ordenada na tela 

listanum = []
maior,menor = 0, 0

for i in range(0, 5):

    num = int(input("Digite um valor: "))

    if i == 0 or num > listanum[- 1]: #  OU se o número for maior do que o número que está no último index
        listanum.append(num)

    else:
        posicao = 0
        while posicao < len(listanum): # vai da posição zero até a última posição
            if num <= listanum[posicao]: # se o número for menor que outro valor da posição esse novo número vai ser adicionado antes do maior valor 
                listanum.insert(posicao, num)
                break
            
            posicao += 1 

print(listanum)