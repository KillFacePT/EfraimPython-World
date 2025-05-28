
# crie um programa que tenha uma tupla com várias palavras(não suar acentos)
# depois disso, deve mostrar, para cada palavra, quais são as suas vogais 

palavras = ("Arroz", "Feijao", "Estudar", "Correr", "Celular", "Python")

vogais = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")


for p in palavras:
    vogais_na_palavra = [] # cria uma lista vazia
    
    for letra in p:
        if letra in vogais: # verefica se na palavra tem vogal e adiciona a vogal na lista usando o append()
            vogais_na_palavra.append(letra)
    
    print(f"Na palavra {p.upper()} temos as vogais {" ".join(vogais_na_palavra)} ") # vai dar join nas vogais em uma string com um espaço 

# join() pega todos os itens em uma lista e une em uma string

'''
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end='') # esse end não quebra linha para as vogais da mesma palavra printam na mesma linha

    for letra in p:
        if letra.lower() in 'aeiou': # a própria palavra é uma lista de strings 
            print(letra, end=" ") # esse end printa as vogais na mesma linha com um espaço 

'''