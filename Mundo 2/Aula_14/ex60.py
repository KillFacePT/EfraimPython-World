
# faça um programa que leia um número qualquer e mostre o seu fatorial
# 5! = 5x4x3x2x1 = 120 

# from math import factorial

num = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1
numero = num 

while numero > 0:

    fatorial = fatorial * (numero)
  
    numero -= 1

print(f"Calculando {num}! = ", end="")

for i in range(num, 0, -1):

    print(f"{i} x ", end="")
print(f"= {fatorial:,}")

