
# melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10
# só que agora o jogador vai tentar adivinha até acertar 
# mostrando no final quantos palpites foram necessários para vencer

from random import randint

num = randint(0, 10)

print("-=-" * 20)
print("Vou pensar em um número entra 0 e 10. Tente adivinhar...")
print("-=-" * 20)

numero_escolhido = int(input("Qual é o número: "))
tentaiva = 1

while numero_escolhido != num:
    if numero_escolhido < num:
        numero_escolhido = int(input("Mais... Tente de novo: "))

    elif numero_escolhido > num:
        numero_escolhido = int(input("Menos... Tende de novo: "))

    tentaiva += 1

print(f"Acertou com {tentaiva} tentativas")
print("ACERTOU !!!")


'''
computador = randint(0, 10)
acertou = False

palpites = 0
while not acertou: # enquanto nao acertou, a hora que acertar for True o while vira false e sai do loop 
    jogador = int(input("Qual seu palpite? "))
    palpites += 1

    if jogador == computador:
        acertou = True

    else:
        if jogador < computador:
            print("Mais... Tente de novo")

        elif jogador > computador:
            print("Menos... Tente de novo")
print(f"Acertou com {palpites} palpites.")
'''