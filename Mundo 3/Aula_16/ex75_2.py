
numero = (int(input("Digite 1º número: ")),
          int(input("Digite 2º número: ")),
          int(input("Digite 3º número: ")),
          int(input("Digite 4º número: ")))

print(f"Você digitou os valores {numero}")
print(f"O valor 9 apareceu {numero.count(9)} vezes")

if 3 in numero:
    print(f"O valor 3 apareceu na {numero.index(3) + 1}ª posição")
else:
    print(f"O valor 3 não foi digitado em nenhuma posição")

print("Os valores pares digitados foram ", end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')

