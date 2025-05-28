
# faça um programa que ajude um jogador da mega sena a criar palpites
# o programa vai perguntar quantos jogos seão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint


print("-" * 30)
print(f"{"MEGA SENA":^30}")
print("-" * 30)

quant = int(input("Quantos jogos você quer que eu sorteie? "))

print(" ")
print("-=" * 5, f"{f"SORTEANDO {quant} JOGOS"}", "-=" * 5)
print(" ")

pedras = []

for s in range(quant):
    
    for _ in range(6):
        num = randint(1, 60)
        if num not in pedras:
            pedras.append(num) # não deixa repetir número

    pedras.sort()
    print(f"Jogo {s + 1}: {pedras}")
    pedras.clear()  

print(" ")
print("-=" * 5, f"{"< BOA SORTE! >"}", "-=" * 5)