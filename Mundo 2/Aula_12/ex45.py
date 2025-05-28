
# Crie um programa que faca o computador jogar JOkenpô com voce
import random
from time import sleep

jokenpo = ['Pedra', 'Papel', 'Tesoura']

computador = random.choice(jokenpo)

print('''Suas opções: 
[0] PEDRA 
[1] PAPEL 
[2] TESOURA''')

jogador = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
print('-=' * 11)
print(f"Computador jogou {computador}")
print(f"Jogador jogou {jokenpo[jogador]}")
print('-=' * 11)


if computador == jokenpo[0]:  # computador jogou pedra
    if jogador == 0:
        print("Empate")
    
    elif jogador == 1:
        print("Jogador Vence")

    elif jogador == 2:
        print("Computador Vence")

elif computador == jokenpo[1]: # computador jogou papel
    if jogador == 0:
        print("Computador Vence")

    elif jogador == 1:
        print("Empate")

    elif jogador == 2:
        print("Jogador Vence")

elif computador == jokenpo[2]: # computador jogou tesoura
    if jogador == 0:
        print("Jogador Venceu")

    elif jogador == 1:
        print("Computador Vence")

    elif jogador == 2:
        print("Empate")

