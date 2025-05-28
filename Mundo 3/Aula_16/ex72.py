
# crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso de zero até vinte
# seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso

tuplas_num = ("zero", "um", "dois", "três", 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
   
while True:
    
    num = int(input("Digite um número de 0 a 20: "))

    if num <=20 and num >=0:
        break
    print("Tente Novamente. ", end="") 
    
print(f"Você digitou o número {tuplas_num[num]}")
