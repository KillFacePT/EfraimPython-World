
# crie um programa que vai ler vários números e colocar em uma lista
# depois disso, mostre:
# a) quantos números foram digitados
# b) a lista de valores, ordenada de forma decrescente
# c) se o valor 5 foi digitado e está ou não na lista 

lista_num = []
quant_digiado = 0

while True:
    
    num = int(input("Digite um número: "))

    lista_num.append(num)

    # lista_num.append(int(input("Digite um número: ")))

    continuar = ' '
    while continuar not in "sn":
       continuar = str(input("Deseja continuar? [S/N] ")).strip().lower()[0]

    quant_digiado += 1

    if continuar in "n":
        break

# print(len(lista_num))

print(f"Foram digitados {quant_digiado} números")

lista_num.sort(reverse=True)
print(lista_num)

if 5 in lista_num:
    print(f"O valor 5 foi digitado e encontra-se na posição {lista_num.index(5) + 1}")

else:
    print("O valor 5 não foi adicionado")