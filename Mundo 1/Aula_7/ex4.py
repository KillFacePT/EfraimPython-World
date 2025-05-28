
# Faça um programa que leia algo pelo teclado e mostre na tela 
# o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input("Digite algo: ")

print(type(x))
print("So tem espaços? ", x.isspace())
print("É um número ? ",x.isnumeric())
print("É alfabético? ", x.isalpha())
print("É alfanumérico? ", x.isalnum())
print("Está em maiúsculas? ", x.isupper())
print("Está em minúsculas? ", x.islower())
print("Está capitalizada ? ", x.istitle())