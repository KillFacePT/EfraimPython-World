
# crie um programa que leia vários números inteiros pelo teclado
# no final da execução, mostre a média entre todos os valores 
# e qual foi o maior e o menor valores lidos
# o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

contagem = 0
soma = 0
continuar = 's'
numero = 0

maior = 0 
menor = 0 
lista = []


while continuar != 'n':

    numero = int(input("Digite um número: "))
    continuar = str(input("Deseja Continuar? [S/N] ")).lower()

    if continuar == 's':

        soma += numero
        contagem +=1 

    
    elif continuar != 's' and continuar != 'n':
        print("Você digitou errado. Por favor escolha 'S' para sim e 'N' para não")
        continuar = str(input("Deseja Continuar? [S/N] ")).lower()
        soma += numero
        contagem +=1 

    else:
        soma += numero
        contagem +=1 
        print("SAIR")

     
    lista += [numero]

media = soma / contagem

print('O Maior número:', max(lista))  #maximo valor da lista
print('O Menor número:', min(lista))  #minimo valor da lista
print(f"{media:.2f}")

'''
continuar = "S"

while continuar in "Ss":

    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
'''

'''
if contagem == 1:
    maior = menor = numero

else:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero
'''