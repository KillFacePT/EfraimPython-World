
# Crie um programa que vai ler vários números e colocar em uma lista
# depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente
# ao final, mostre o conteúdo das três listas geradas

lista = []
lista_par = []
lista_impar = []

while True:
    
    num = int(input("Digite um número: "))

    lista.append(num)

    continuar = str(input("Deseja continuar? [S/N] ")).strip().lower()[0]
    if continuar in "n":
        break

for n in lista:
    if n % 2 == 0:
        lista_par.append(n)

    else:
        lista_impar.append(n)

print(f"A lista completa é {lista}")
print(f"A lista de pares é {lista_par}")
print(f"A lista de impares é {lista_impar}")
