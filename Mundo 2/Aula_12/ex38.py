
# escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# o primeiro valor é maior
# o segundo valor é maior
# nao existe valor maior, os dois são iguais 

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

if n1 > n2:
    print(f"O primeiro valor {n1} é maior que o segundo valor {n2}")

elif n2 > n1:
    print(f"O segundo valor {n2} é maior que o primeiro valor {n1}")

else:
    print(f"Não existe valor maior, os dois valores {n1} e {n2} são iguais")