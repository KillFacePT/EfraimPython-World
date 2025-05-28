
# Crie um programa que leia vários números inteiros pelo teclado
# o programa só vai para quando o usuário digitar o valor 999, que é a condição de parada
# no final, mostre quantos números foram digitados e qual foi a soma entre eles
# desconsiderando o flag(999)



print("-=" * 30)
print("Digite um número qualquer. Digite 999 para sair.")
print("-=" * 30)


contagem = 0
soma = 0
n = 0
zero = 0

while n != 999:

    n = int(input("Digite um número interio: "))

    if n != 999:
    
        soma += n

        contagem += 1 

        print(f'{zero} + {n}')
        print(f"Soma = {soma}")

        zero += n

    else:
        print("999 P/SAIR\n")


print(f"Foram digitados {contagem} números e a soma desses números é {soma}")