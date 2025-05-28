
# crie um programa que simule o funcionamento de um caixa eletrônico
# no inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues
# OBS: considere que o caixa possui cédulas de 50, 20, 10 e 1
print("=" * 40)
print(f"{"SACAR DOLETAS":^40}")
print("=" * 40)


contagem_50 = contagem_20 = contagem_10 = contagem_1 =0
sacar = int(input("Quanto deseja sacar? R$: "))

while True:
    
    while sacar >= 50:
        sacar -= 50
        contagem_50 += 1

    while sacar >= 20:
        sacar -= 20
        contagem_20 += 1

    while sacar >= 10:
        sacar -= 10
        contagem_10 += 1

    while sacar >= 1:
        sacar -= 1
        contagem_1 += 1

    if sacar == 0:
        break

print(f"Total de {contagem_50} de R$:50")
print(f"Total de {contagem_20} de R$:20")
print(f"Total de {contagem_10} de R$:10")
print(f"Total de {contagem_1} de R$:1")
print("Volte Sempre")

'''
while True:

    if sacar >= 50: # sacando notas de 50
        sacar -= 50
        contagem_50 += 1
    
    # senão der para sacar mais notas de 50 vai para a proxima que é 20 e assim por diante 20 para 10 e 10 para 1
    #else:
    elif sacar >= 20:
        sacar -= 20
        contagem_20 += 1

    elif sacar >= 10:
        sacar -= 10
        contagem_10 += 1

    elif sacar >= 1:
        sacar -= 1
        contagem_1 += 1

    if sacar == 0:
        break

print(f"Total de {contagem_50} de R$:50")
print(f"Total de {contagem_20} de R$:20")
print(f"Total de {contagem_10} de R$:10")
print(f"Total de {contagem_1} de R$:1")
print("Volte Sempre")
'''