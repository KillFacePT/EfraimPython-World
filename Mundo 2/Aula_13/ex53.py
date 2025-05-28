
# crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input("Digite uma frase: ")).replace(" ", "").upper()

palavra = frase.replace(" ", "")

inverso = ''
                    #len é a quantidade de letras
                    # -1 é até a primeira letra que é 0
                    # -1 é a contagem das casas no reverso

for letra in range(len(palavra) -1, -1, -1):#len está com menos um porque o index começa do zero (ex:20 letras -> 0-19 index) 
    
    inverso += palavra[letra]

print(f"O inverso de {frase} é {inverso}")

if inverso == palavra:
    print(" ")
    print("Tem palíndromo")

else:
    print(" ")
    print("Não tem palíndromo")

print(" ")

'''
frase = str(input("Digite uma frase: ")).replace(" ", "").upper()

palavra = frase.replace(" ", "")

inverso = [::-1] # fatiamento não precisa usar o for
print(f"O inverso de {frase} é {inverso}")
'''

'''
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split() # split() transforma em lista
junto = ''.join(palavras)
'''