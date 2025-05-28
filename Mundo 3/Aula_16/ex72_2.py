
# continuação desafio (deseja continuar)

tuplas_num = ("zero", "um", "dois", "três", 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')



while True:
    
    num = int(input("Digite um número de 0 a 20: "))


    if num <=20 and num >=0:
        print(f"Você digitou o número {tuplas_num[num]}") 

        continuar = ' '   
        while continuar not in "sn":
            continuar = str(input("Deseja continuar? [S/N] ")).strip().lower()[0]  
        
        if continuar == 'n':
            break
    
    else:
        print("Tente novamente.", end='')