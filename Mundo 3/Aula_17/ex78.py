
# faça um programa que leia 5 valores numéricos e guarde-os em uma lista 
# no final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lsta

numeros_lista = []

for n in range(1, 6):
    numeros_lista.append(int(input(f"DIgite um número para a posição {n}: ")))

print(f'Você digitou os valores {numeros_lista}')

print(f"O maior número da lista é {max(numeros_lista)} nas posições: ", end='')


maior_num = max(numeros_lista)
menor_num = min(numeros_lista)

for i, valor in enumerate(numeros_lista):
    if valor == maior_num:
        print((i + 1), end='...')

print(f"\nO menor número da lista é {min(numeros_lista)} nas posições: ", end="")
for i, valor in enumerate(numeros_lista):        
    if valor == menor_num:
        print((i + 1), end='...')



# conferindo maior e menor
listanum = []
maior, menor = 0
for c in range(1, 6):
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]

        if listanum[c] < menor:
            menor = listanum[c]
            