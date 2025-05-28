
import random
from time import sleep

jokenpo = ['none' , 'Pedra', 'Papel', 'Tesoura']

computador = random.choice(jokenpo[1:4])

print('''Suas opções: 
[1] PEDRA 
[2] PAPEL 
[3] TESOURA''')

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



if computador == jokenpo[1]:  # computador jogou pedra
    if jogador == 1:
        print("Empate")
    
    elif jogador == 2:
        print("Jogador Vence")

    elif jogador == 3:
        print("Computador Vence")

elif computador == jokenpo[2]: # computador jogou papel
    if jogador == 1:
        print("Computador Vence")

    elif jogador == 2:
        print("Empate")

    elif jogador == 3:
        print("Jogador Vence")

elif computador == jokenpo[3]: # computador jogou tesoura
    if jogador == 1:
        print("Jogador Venceu")

    elif jogador == 2:
        print("Computador Vence")

    elif jogador == 3:
        print("Empate")