
# faça um programa que leia o peso de cinco pessoas
# no final mostre qual foi o maior e o menor peso 

maior = 0 
menor = 0 

for i in range(1, 6):
    peso = float(input(f"Peso {i}ª pessoa: "))


# quando um número é adicionado ele vai ser tanto maior e menor até o momento que vier outro número
# quando o outro número for maior ou menor ele passa a ter a posição de maior ou menor 
    if i == 1:
        maior = peso # lendo o primeiro peso que é tanto maior e menor
        menor = peso

    else:
        if peso > maior: # primeiro número lido 7, segundo 9. 9 é maior que 7
            maior = peso

        if peso < menor: # primeiro número lido 3, segundo 4. 3 é menor que 4
            menor = peso
    
print(f"O maior peso é {maior} Kg")
print(f"O menor peso é {menor} Kg")


'''
pesos = []
for i in range(1,6):
    peso = float(input(f"Qual o peso da {i}ª pessoa? "))
    pesos += [peso]
pesos.sort()
print(f'O maior peso lido foi de {pesos[4]} Kg e o menor peso foi de {pesos[0]}')

'''

'''
lst=[]  #lista vazia
for c in range(1, 6):
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    lst+=[peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lst))  #maximo valor da lista
print('O Menor peso foi:', min(lst))  #minimo valor da lista
'''