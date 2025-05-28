
# faca um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input("Escolha o primeiro numero: "))
n2 = int(input("Escolha o segundo numero: "))
n3 = int(input("Escolha o terceiro numero: "))

if n1 > n2 and n1 > n3 and n2 > n3:
    print(f"{n1} é o maior número  \n{n3} é o menor número.")

elif n1 > n2 and n1 > n3 and n3 > n2:
    print(f"{n1} é o maior número \n{n2} é o menor número.")


elif n2 > n1 and n2 > n3 and n3 > n1:
    print(f"{n2} é o maior número \n{n1} é o menor número.")

elif n2 > n1 and n2 > n3 and n1 > n3:
    print(f"{n2} é o maior número \n{n3} é o menor número.")


elif n3 > n1 and n3 > n2 and n1 > n2:
    print(f"{n3} é o maior número \n{n2} é o menor número.")

elif n3 > n2 and n3 > n2 and n2 > n1:
    print(f"{n3} é o maior número \n{n1} é o menor número.")


