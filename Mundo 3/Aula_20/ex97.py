
# faça um programa que tenha uma função chamada escreva()
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
# ex: escreva("Ola mundo")
# saida: 
# ~~~~~~~~~
# ola mundo
# ~~~~~~~~~

def escreva(txt):
    print("~" * len(texto))
    print(txt)
    print("~" * len(texto))

    #bonitinho
    tam = len(texto) + 4
    print("~" * tam)
    print(f"  {txt}")
    print("~" * tam)

texto = str(input("Digite uma frase: ")).strip()
# tamanho_texto = len(texto)
escreva(texto)