
# faça um programa que jogue par ou impar com o computador
# o jogo só será interrompido quando o jogador PERDER
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint
from time import sleep

print("=-" * 15)
print(f"{"PAR OU ÍMPAR":^30}")
print("=-" * 15)

vitoria = 0

while True:

    num = int(input("Diga um valor: "))

    impar_par = str(input("Par ou Ímpar? [P/I] ")).lower()

    if impar_par != 'p' and impar_par != 'i':
        print("Por favor digite apenas as opções [P/I]")
        impar_par = str(input("Par ou Ímpar? [P/I] ")).lower()

    print("Aguarde 3 segundos poque estou escolhendo meu valor")
    
    for i in range(3, 0, -1):
        print(i)
        sleep(1)
    
    num_maquina = randint(1, 10)

    soma = num + num_maquina
    
    if soma % 2 == 0:
        print(f"Você jogou {num} e Eu o computador {num_maquina}")
        print(f"Total de {soma} DEU PAR")
        
        if impar_par == 'p':
            print("Você VENCEU !!!")
            print("Vamos Jogar novamente ?")

        elif impar_par == 'i':
            break
            
        vitoria =+ 1

    elif soma % 2 == 1:
        
        print(f"Você jogou {num} e Eu o computador {num_maquina}")
        print(f"Total de {soma} DEU ÍMPAR")
        
        if impar_par == 'i':
            print("Você VENCEU !!!")
            print("Vamos Jogar novamente ?")

        elif impar_par == 'p':
            break

        vitoria =+ 1
    

print("Você PERDEU !!!")
print("=-" *15)
print(f"Game Over ! Você venceu {vitoria} vezes")

'''
white True:
    impar_par = ' '

    while impar_par not in 'PI':
        impar_par = str("par ou Ímpar? [P/I]).strip().upper()[0]
    
    if impar_par == "P":
        if soma % 2 == 0:
            print("Voce venceu")
            vitoria += 1
        else:
        print("Perdeu")
        break
        
    elif impar_par == "I":
        if soma % 2 == 1:
            print("Voce venceu")
            vitoria += 1
        else:
        print("Perdeu")
        break

'''