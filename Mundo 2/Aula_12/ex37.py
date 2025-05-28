
# escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher quqal sera a base de conversão:

# 1- binário 2- octal 3- hexadecial 

num = int(input("Digite um número: "))
print(" ")
print("Escolha a base de conversão:")
conv = str(input("[1] para binário, [2] para octal, [3] para hexa: "))

if conv == str(1):
    print(f"O número {num} convertido para BINARIO é {bin(num[2:])}")

elif conv == str(2):
    print(f"O número {num} convertido para OCTAL é {oct(num)}")

elif conv == str(3):
    print(f"O número {num} convertido para HEXA é {hex(num)}")

else:
    print("Nenhuma das opções escolhidas.")