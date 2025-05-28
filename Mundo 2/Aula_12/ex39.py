
# faça um programa que leia o ano de nascimento de um jovem e informe, de com acordo com sua idade 
# se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar
# se ja passou do tempo do alistamento 
# o programa tambem deverá mostrar o tempo que falta ou que passou do prazo 


from datetime import date

ano_nasc = int(input("Qual ano você nasceu? "))

ano_atual = date.today().year

idade = ano_atual - ano_nasc

print(" ")
print(f"Nascimento: {ano_nasc}")
print(f"Sua idade: {idade}")
print(" ")

if idade > 18:
    prazo = idade - 18
    print(f"Você ja passou do prazo de {prazo} ano(s) para o alistamento.")

elif idade < 18:
    prazo = 18 - idade
    alista = ano_atual + prazo
    print(f"Voce irá se alistar em {prazo} ano(s) em {alista}")

elif idade == 18:
    print(f"Você está com {idade} anos e está na hora de se alistar.")
