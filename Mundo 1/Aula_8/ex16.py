
# Crie um programa que leia um numero Real qualquer pelo teclado
# e mostra na tela a sua porção inteira 

from math import floor, trunc

n = float(input("Digite um número: "))

print(f"O número: {n} tem a parte inteira {floor(n)}")
print(f"O número: {n} tem a parte inteira {trunc(n)}")

# trunc() retorna x com a parte fracionária removida
#floor() é para x positivos 
