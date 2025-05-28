
# crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
# caso onúmero já exista lá dentro, elenão será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente

lista_num = []

while True:
    
    num = int(input("Digite um número: "))

    if num not in lista_num:
        lista_num.append(num)
        print("Valor adicionado com sucesso...")

    else:
        print("Valor duplicado! Não vou adicionar ")

    continuar = ' '
    while continuar not in "sn":
       continuar = str(input("Deseja continuar? [S/N] ")).lower()[0]

    if continuar == 'n':
        break

    #if continuar in "n":
    #    break

lista_num.sort()
print(f"Você digitou os valores {lista_num}")