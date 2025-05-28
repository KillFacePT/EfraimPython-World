# Faça um programa que leia um número Inteiro e mostre na tela 
# o seu sucessor e seu antecessor 

num = int(input("Digite um número: "))

antecessor_num = num -1 

sucessor_num = num + 1 

print(f"Numero digitado foi:{num} \nseu numero antecessor é: {antecessor_num} \nseu número sucessor é: {sucessor_num}")

# somente com uma variavel 
print(" ")
print(f"Numero digitado foi:{num} \nseu numero antecessor é: {num -1} \nseu número sucessor é: {num + 1}")