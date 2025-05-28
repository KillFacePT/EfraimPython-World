
# faça um programa que leia o nome complete de uma pessoa
# msotrando em seguida o primeiro e o ultimo nome separadamente

nome = str(input("Digite seu nome completo: ")).strip()

name = nome.split()

print(name)

print(f"Seu primeiro nome é: {name[0]}")
print(f"Seu ultimo nome é: {name[-1]}") 

# modo alternativo  -- (name[len(name) - 1])
print(f"Seu ultimo nome é: {name[len(name) -1]}")  