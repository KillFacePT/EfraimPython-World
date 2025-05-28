
# faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez
# em que posição ela aparece a última vez 

frase = str(input("Escreva uma frase: ")).lower()

print(f"A vogal 'A' aparece: {frase.count("a")} vezes")
print(f"Sua posição inicial é: {frase.find("a")}")
print(f"Sua posição final é: {frase.rfind("a")}")