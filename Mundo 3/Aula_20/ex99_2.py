
from time import sleep

def maior(*num):
    print("-=" * 15)
    print("Analisando os valores passados...")
    contador = maior = 0 

    for x in num:
        print(f"{x}", end=' ', flush=True)
        sleep(0.5)
        contador += 1

        if len(num) == 0:
            maior = 0
        else:
            maior = max(num)
            
# if len(num) >= 1:
#         maior = max(num)
#     else:
#         maior = 0

    #maior = max(num)
    print(f"Foram informados {contador} valores ao todo")
    print(f"O maior valor informado foi: {maior}")


maior(5, 3, 8, 1)
maior(9, 1, 0, 15, 23)
maior(3)
maior()