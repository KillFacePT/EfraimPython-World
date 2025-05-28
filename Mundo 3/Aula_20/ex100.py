
# faça um programa que tenha uma lista chamda números e duas funções chamadas sorteia()
# e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
# e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior

from random import randint
from time import sleep

numeros = []
pares = []

def sorteia(x):

    print("Sorteando 5 valores na lista: ", end='')
    for i in range(x):
        i = randint(1, 10)
        print(i, end=' ', flush=True)
        sleep(0.5)
        numeros.append(i)
        #print(i)
    #print(numeros)
    print()

def somapar(num):

    soma = 0
    # for i in range(len(num)):
    #     if num[i] % 2 == 0:
    #         soma += num[i]

    #     if num[i] % 2 == 0:
    #         pares.append(num[i])

    for i in num:
        if i %2 == 0:
            soma += i

        if i % 2 == 0:
            pares.append(i)

    print(f"A soma dos valores pares {pares} é: {soma}")

sorteia(5)
somapar(numeros)