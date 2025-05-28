
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome 

nome = str(input("Digite seu nome completo: "))

primeiro_nome = nome.split() # cria uma lista de strings

print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ", "")))
print(nome.find(" ")) # vai parar a contagem no primeiro espaço em branco 
print(len(primeiro_nome[0]))