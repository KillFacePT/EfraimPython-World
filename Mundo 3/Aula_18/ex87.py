
# aprimore o desafio antetior: mostando no final:
# a) a soma de todos os valores pares digitados
# b) a soma dos valores da terceira coluna
# c) o maior valor da segunda linha 

matriz = [[], [], []]
soma_par = 0
soma = 0
maior = menor = 0

for l in range(0, 3):

    for c in range(0, 3):
        num = (int(input(f"Digite um valor para [{l}, {c}]: "))) 

        matriz[l].append(num)
        
        if num % 2 == 0:
            soma_par += num

        if c == 2:
            soma += num

        if num in matriz[1]: # if l == 1:
            if c == 0:
                maior = menor = num
            else:
                if num > maior:
                    maior = num

                if num < menor:
                    menor = num

print("-=" * 30)

for l in range(0, 3):

    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")  
    print()

print('-=' * 30)
print(f"A soma dos números pares digitados foi de: {soma_par}")
print(f"A soma dos valores da terceira coluna é: {soma}")
print(f"O maior numero da 2ª é: {maior}")