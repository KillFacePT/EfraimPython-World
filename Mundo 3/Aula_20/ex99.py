
# faça um program que tenha uma função chamada maior()
# que receba vários parâmetros com valores inteiros
# seu programa tem que analisar todos os valores e dizer qual deles é o maior 

# quantidade = int(input("Quantos números quer digitar: "))

# for i in range(quantidade):
#     n = int(input(f"Digite o {i + 1} numero: "))
from time import sleep

def maior(*num):
    print("-=" * 15)
    print("Analisando os valores passados...")
    contador = maior = 0 

    for x in num:
        print(f"{x}", end=' ', flush=True)
        sleep(0.5)
        #contador += 1

        if contador == 0:
            maior = x 
        else:
            if x > maior:
                maior = x
        contador += 1

    #maior = max(num)
    print(f"Foram informados {contador} valores ao todo")
    print(f"O maior valor informado foi: {maior}")


maior(5, 3, 8, 1)
maior(9, 1, 0, 15, 23)
maior(3)
maior()

# maior = contador = 0

# for...
    # if contador == 0:
    #     maior = x 
    # else:
    #     if valor > maior:
    #         maior = valor 
    # contador += 1

# if len(num) >= 1:
#         maior = max(num)
#     else:
#         maior = 0