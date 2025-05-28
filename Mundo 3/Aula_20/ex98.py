
# faça um programa que tenha função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem
# seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(i, f, s):
    for i in range(i, f, s):
        print(i, end=" ")
        # sleep(1)
    print()

print("-=" * 20)
contador(1, 11, 1)

print("-=" * 20)
contador(10, -1, -2)

print("-=" * 20)
print("Agora é sua vez de personalizar a contagem!")

inicio = int(input("Inicio do contador: "))
fim = int(input("Fim do contador: "))
step = int(input("Passo do contador: "))

if inicio > fim:
    if step > 0:
        step *= -1

if step == 0:
    step = 1
    if inicio > fim:
        if step > 0:
            step *= -1


print("-=" * 20)
print(f"A contagem de {inicio} até {fim} em passo de {step}:")
contador(inicio, fim, step)