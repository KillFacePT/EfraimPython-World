
# crie um programa que leia vários números inteiros pelo teclado
# o programa só vai parar quando o usuário digitar o valor 999
# que é a condição de parada.
# no final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
n = 0 
soma = 0
contagem = 0

while True:

    n = int(input("Digite um número: "))

    if n == 999:
        break

    soma += n
    contagem += 1

print(f"Você digitou {contagem} número(s) e a soma é {soma}")