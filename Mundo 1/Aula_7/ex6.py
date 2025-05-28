
# Crie um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada

num = int(input("Digite um número: "))

num_duble = num * 2

num_triple = num * 3

num_raiz = num ** (1/2)

print(f"Número digitado: {num} \nSeu dobro é: {num_duble} \nSeu triplo é: {num_triple} \nSua raiz quadrada é: {num_raiz:.2f}")

print(" ")
print("O dobro de {} vale {}".format(num, num_duble))
print("O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.".format(num, num_triple, num, num_raiz))

# sem variaveis

print(" ")
print("O dobdro de {} vale {}".format(num, num *2))
print("O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.".format(num, num *3, num, num **(1/2)))

# funcao de potencia "pow"

print(" ")
print("A raiz quadrada de {} é igual a {:.2f}.".format(num, pow(num, (1/2))))