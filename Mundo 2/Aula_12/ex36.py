
# escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valor_casa = float(input("Qual o preço da casa que deseja comprar? "))

salario = float(input("Qual o seu salário? "))

anos = int(input("Quantos anos deseja pagar? "))

prestacao = valor_casa / (anos * 12)

print(f"Prestação R$: {prestacao:.2f}")

if prestacao > (salario * 0.3):
    print("EMPRESTIMO NEGADO")
    print("A prestação exede 30% do seu salário")

else:
    print("EMPRESTIMO APROVADO")


'''
if prestacao <= (salario * 0.3):
    print("EMPRESTIMO APROVADO")
    

else:
    print("EMPRESTIMO NEGADO")
    print("A prestação exede 30% do seu salário")
'''