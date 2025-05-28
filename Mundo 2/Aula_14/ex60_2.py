
# faça um programa que leia um número qualquer e mostre o seu fatorial
# 5! = 5x4x3x2x1 = 120 

# from math import factorial


num = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1
numero = num 

print(f"Calculando {num}! = ", end="")
while numero > 0:
    
    print(f"{numero}", end="")
    print(" x " if numero > 1 else " = ", end="") # Escrevendo if em print é a mesma coisa da condiçao abaixo 
    
    '''
    if numero > 1:
        print(" x ", end="")
    else:
        print(" = ", end="")
    '''

    fatorial *= numero
    numero -= 1
print(f"{fatorial}")


# FOR 
num = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
numero = num
print(f"Calculando {num}! = ", end="")
for c in range(num, 0, -1):

    print(f"{numero}", end="")
    if numero > 1:
        print(" x ", end="")
    else:
        print(" = ", end="")

    fatorial *= numero
    numero -= 1
print(f"{fatorial}")