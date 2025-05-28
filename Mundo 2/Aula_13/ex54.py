
# Crie um programa que leia o ano de nascimento de sete pessoas
# no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date

ano_atual = date.today().year

maior_idade = 0
menor_idade = 0

for i in range(1, 8):
    ano_nascimento = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    
    idade = ano_atual - ano_nascimento

    print(f"Nascimento: {ano_nascimento}, Idade: {idade}")
    
    if idade >=18:
        maior_idade += 1 
        print("Maior de idade\n")

    else:
        menor_idade += 1
        print("Menor de idade\n")

print(f"Ao todo se encontra {maior_idade} maiores de idade e {menor_idade} menores de idade.")