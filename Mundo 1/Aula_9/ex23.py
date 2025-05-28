
# Faça um  programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos digitos separados 
# matematicamente e strings 

num = int(input("Digite um número: "))

u = num // 1 % 10  # tiro o resto da divisão por dez que sempre vai me retornar no valor da unidade
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}")


'''
nao funciona porque se digitar um numero com duas casas apenas gera um erro
print(f"Unidade: {num[3]}")
print(f"Dezena: {num[2]}")
print(f"Centena: {num[1]}")
print(f"Milhar: {num[0]}")
'''

print(u * 1)