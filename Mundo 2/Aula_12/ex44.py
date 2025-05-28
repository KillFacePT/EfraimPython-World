
# elabore um programa que calcule o valor a ser pago por um produto 
# considerando o seu preço normal e condição de pagamento:

# à vista dinheiro: 10% desconto
# à vista no cartão: 5% desconto
# em ate 2x no cartão: preço normal
# 3x ou mais no cartão: 20% juros 

print('{:=^40}'.format("LOJAS EFRAIM"))
print(f"")

preco = float(input("Qual o preço do produto? "))

pagamento = int(input("FORMAS DE PAGAMENTO \n[1]Dinheiro \n[2] A vista no cartão \n[3]2x no cartão \n[4] 3x ou mais no cartão \nDigite o numero de sua forma de pagamento: "))

if pagamento == 1:
    desconto = preco - (preco *0.1)
    print(f"Sua compra de {preco} vai custar {desconto}")

elif pagamento == 2:
    desconto = preco - (preco *0.05)
    print(f"Sua compra de {preco} vai custar {desconto}")

elif pagamento == 3:
    print(f"Preço normal")

elif pagamento == 4:
    parcelas = int(input("Quantas parcelas? "))
    juros = (preco / parcelas) + ((preco / parcelas)* 0.20)
    preco_final = preco + (preco * 0.2)
    print(f"Sua compra será parcelada em {parcelas}x de {juros:.2f} com juros")
    print(f"Sua compra de {preco:.2f} vai custar {preco_final:.2f}")


'''
if pagamento == 1:
    preco_final = preco - (preco *0.1)

elif pagamento == 2:
    preco_final = preco - (preco *0.05)
    

elif pagamento == 3:
    preco_final = preco
    parcela = preco / 2
    print(f"Sua compra sera parcelada em 2x de {parcela} ")

elif pagamento == 4:
    parcelas = int(input("Quantas parcelas? "))
    juros = (preco / parcelas) + ((preco / parcelas)* 0.20)
    preco_final = preco + (preco * 0.2)
    print(f"Sua compra será parcelada em {parcelas}x de {juros:.2f} com juros")

print(f"Sua compra de {preco:.2f} vai custar {preco_final:.2f}"

'''