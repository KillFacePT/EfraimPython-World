
# crie um programa que leia Dois Valores e mostre um Menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# seu programa deverá realizar a operação solicitada em cada caso
from time import sleep

num1 = int(input("Digite o 1º valor: "))
num2 = int(input("Digite o 2º valor: "))

print("-=" * 10)
print(f"{"MENU":^20}") # :^10 quantidade de espaços
print("-=" * 10)

menu = 0

while menu != 5:

    menu = int(input("[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do programa \nQual opção deseja escolher: "))
    
    if menu == 1:
        soma = num1 + num2
        print("\nVoce escolheu Somar")
        print(f"A soma de {num1} + {num2} é igual a {soma}")

    elif menu == 2:
        multi = num1 * num2
        print("\nVocê escolher Multiplicar")
        print(f"A multiplicação de {num1} x {num2} é igual a {multi}")

    elif menu == 3:
        if num1 > num2:
            print("\nVocê escolheu comparação de número maior")
            print(f"O número {num1} é maior que o número {num2}")
        elif num1 < num2:
            print("\nVocê escolheu comparação de número maior")
            print(f"O número {num2} é maior que o número {num1}")
        else:
            print(f"\nOs 1º valor {num1} e o 2º valor {num2} são iguais")
                  
    
    elif menu == 4:
        print("\nVocê escolheu em trocar para novos valores")
        num1 = int(input("Digite o 1º novo valor: "))
        num2 = int(input("Digite o 2º novo valor: "))
        print(f"Novo 1º valor {num1}, novo 2º valor {num2}")

    elif menu > 5:
        print("\nOpção invalida tente de novo: ")

    print("=-=" * 10)

print("\nSair do programa")
print("Contagem para desligar")
for c in range(3, 0, -1):
    print(c)
    sleep(1)
print("Off")
