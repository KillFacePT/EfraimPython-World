
# desenvolva um programa que leia quatros valores pelo teclado e guarde-os em uma tupla. no final mostre:
# a) quantas vezes apareceu o valor 9
# b) em que posição foi digitado o primero valor 3
# c) quais foram os números pares 

tupla_valores = ()

for n in range(1, 5):
    numeros = int(input(f"Digite o {n}º número: "))

    tupla_valores += (numeros, )


print(f"Você digitou os valores {tupla_valores}")
print(f"O valor 9 apareceu {tupla_valores.count(9)} vezes")

if 3 in tupla_valores:
    print(f"O valor 3 apareceu na {tupla_valores.index(3) + 1}ª posição ")

else:
    print(f"O valor 3 não foi digitado em nenhuma posição")


print("Os valores pares digitados foram ", end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')


#################################################################
# mosta todas as posições onde está o 3 e calcula os numeros pares na tupla
posicao_3 = []

for i in range(len(tupla_valores)):
    if tupla_valores[i] == 3:
        posicao_3.append(str(i + 1)) # Convertendo o índice para string, Adicionando 1 para ajustar as posições 

if 3 in tupla_valores:
    print(f"O número 3 aparece nas posições: {', '.join(posicao_3)}") # .join() está unindo as posições em uma única string, separadas por vírgula

else:
    print(f"O valor 3 não aparece em nenhuma posição")


pares = []
for i in range(len(tupla_valores)):
    if tupla_valores[i] %2 == 0:
        pares.append(str(tupla_valores[i]))

print(f"Os valores pares digitados foram {', '.join(pares)}")   