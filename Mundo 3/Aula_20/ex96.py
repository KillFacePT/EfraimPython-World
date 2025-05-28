
# faça um programa que tenha uma função chamada área()
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno 

def area(larg, comp):
    area = larg * comp
    print(f"A área de seu terreno é de: {area} m²")

print("CONTROLE DE TERRENOS")
print("-" * 20)
l = float(input("Largura: "))
c = float(input("Comprimento: "))

area(l, c)