
# Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço FOR

num = int(input("Digite um número para ver sua tabuada: "))

for n in range(1, 11):
    resultado = num * n 
    print(f"{num} x {n} = {resultado}")

print(" ")

for n in range(1, 11): 
    print(f"{num} x {n} = {num * n}")