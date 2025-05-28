
dados = list()
pessoas = list()
peso_total = list()
pessoas_maior_peso = list()
pessoas_menor_peso  = list()

#Dados inseridos pelo usuário
while True: 
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    while True:
        proximo = str(input('Quer continuar? (S/N):')).strip().upper()
        if proximo in 'SN':
            break
    if proximo == 'N':
        break

#Separando todos os pesos na lista > peso_total
for peso in pessoas: # [['efraim', 80], ['eloah', 60]]
    peso_total.append(peso[1])

#Checando o peso máximo e mínimo 
maior_peso = max(peso_total)
menor_peso = min(peso_total)

#Identificando os respectivos nomes de peso Max/Min
for pes in pessoas: # [['efraim', 80], ['eloah', 60]]
    if pes[1] == maior_peso: # if True: Nome, peso > Max 
        pessoas_maior_peso.append(pes[0]) 
        # p[1] significa posição do peso de cada pessoa. p é o index para cada lista e [1] é o index do peso 

    if pes[1] == menor_peso: #if True: Nome, peso > Min
       pessoas_menor_peso.append(pes[0]) 

print(f'{"=-"*20}\nAo todo, você cadastrou {len(pessoas)} pessoa{"s" if len(pessoas) > 1 else ""}.')

print(f'O maior peso foi de {maior_peso}Kg. Peso de {pessoas_maior_peso}')

print(f'O menor peso foi de {menor_peso}Kg. Peso de {pessoas_menor_peso}')