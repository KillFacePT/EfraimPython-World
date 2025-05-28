
# Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessaria para pintar
# sabendo que cada litro de tinta pinta uma área de 2m^2

largura_parede = float(input("Qual a largura da parede em metros? "))

altura_parede = float(input("Qual a altura da parede em metros ? "))

litro_tinta = 2

area_parede = largura_parede * altura_parede

tinta_neces = area_parede / litro_tinta

print(f"Sua parede tem a dimensão de {largura_parede} x {altura_parede} e sua área é de {area_parede}m²")
print(f"Você ira precisar de {tinta_neces:.2f} litros de tinta")