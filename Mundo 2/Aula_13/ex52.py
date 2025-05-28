
# faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input("Digite um número: "))

total = 0 # numero de divisiveis 

for c in range(1, num + 1):
    if num % c == 0:# print azul
        print("\033[34m", end ='')
        total += 1
    else: # print preto
        print("\033[m", end='')
    print(f"{c} ", end='')

print(f"\n\033[mO numero {num} é divisivel {total} vezes")

if total == 2:
    print("E por isso ele é PRIMO")

else:
    print("Ele não é PRIMO")