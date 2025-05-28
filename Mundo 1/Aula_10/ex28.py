# escreva um programa que faça o computar "pensar" em um numero inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

# o progama deverá escrever na tela se o usuário venceu ou perdeu 

import random
from time import sleep
num = random.randint(0, 5)

print("-=-" * 20)
print("Vou pensar em um número entra 0 e 5. Tente adivinhar...")
print("-=-" * 20)

numero_escolhido = int(input("Escolha um número de 0 a 5: "))

print("PROCESSANDO...")
sleep(3)

if numero_escolhido == num:
    print("Você GANHOU :) !!!")

else:
    print("Você perdeu :(")
