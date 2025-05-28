
# escreva um programa que pergunte o salário de um funcionário e calculo o valor de seu aumento

# para salários superiores a R$: 1250,00 calcule um aumento de 10%

# para inferiores ou iguais, o aumento é de 15% 

salario = float(input("Qual o seu salario? "))

if salario > 1250:
    aumento = salario + (salario * 0.1) 
    print(f"Seu salário foi de R$:{salario} para R$:{aumento}")

else:
    aumento = salario + (salario * 0.15) 
    print(f"Seu salário foi de R$:{salario} para R$:{aumento}")