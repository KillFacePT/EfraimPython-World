
# crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
# depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f"Os valores soteados foram: {numeros}")
print(f"O maior valor soteado foi {max(numeros)}")
print(f"O menor valor soteado foi {min(numeros)}")
print(" ")
print(f"Os valores soteados foram: ", end='')

for n in numeros:
    print(f"{n} ", end='')