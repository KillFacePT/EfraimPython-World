
# crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única 
# que mantenha separados os valores pares e impares.
# no final mostre os valores pares e impares em ordem crescente

numeros = [[], []]

for i in range(1, 8):
    num = int(input(f"{[i]}º Número: "))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print("-=" * 30)
print(numeros)
print("-=" * 30)

numeros[0].sort()
numeros[1].sort()
print(f"Os valores pares são {numeros[0]}")
print(f"Os valores impares são {numeros[1]}")