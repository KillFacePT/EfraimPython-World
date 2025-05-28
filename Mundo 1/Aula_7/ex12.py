
# Faça um algoritmo que leia o preço de um produto e motre sua novo preço
# com 5% de desconto 

print("-----PROMOÇÃO-----")

preco_produto = float(input("Qual o preço do produto ? "))

desconto = preco_produto - (preco_produto * 0.05)  

print(f"O preço do produto em promoção de {preco_produto} para {desconto}")