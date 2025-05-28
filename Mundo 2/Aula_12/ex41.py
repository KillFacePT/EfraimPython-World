
# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:

# ate 9 :mirim
# ate 14: infantil 
# ate 19: junior
# ate 25: senior
# acima: master 

from datetime import date

ano_nasc = int(input("Ano de nascimento: "))

ano_atual = date.today().year

categoria = ano_atual - ano_nasc
idade = ano_atual - ano_nasc

if categoria > 25:
    print(f"Idade: {idade}")
    print("Categoria Master")

elif categoria <= 25:
    print(f"Idade: {idade}")
    print("Categoria Senior")

elif categoria <= 19 and categoria >= 15:
    print(f"Idade: {idade}")
    print("Categoria Junior")

elif categoria <= 14 and categoria >= 10:
    print(f"Idade: {idade}")
    print("Categoria Infantil")

else:
    print(f"Idade: {idade}")
    print("Categoria Mirim")


'''
if categoria <= 9:
    print(f"Idade: {idade}")
    print("Categoria Mirim")
    
elif categoria <= 14:
    print(f"Idade: {idade}")
    print("Categoria Infantil")
    
elif categoria <= 19:
    print(f"Idade: {idade}")
    print("Categoria Junior")

elif categoria <= 25:
    print(f"Idade: {idade}")
    print("Categoria Senior")

else:
    print(f"Idade: {idade}")
    print("Categoria Master")
'''