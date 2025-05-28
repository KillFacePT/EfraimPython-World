
# refaça o desafio 35 dos triângulos, acrescentando o recuros de mostrar que tipo de triângulo será formado

# Equilatero: todos os lados iguais
# Isosceles: dois lados iguais 
# Escaleno: todos os lados diferentes

r1 = float(input("Digite a primeira reta: "))
r2= float(input("Digite a segunda reta: "))
r3 = float(input("Digite a terceira reta: "))
print(" ")

if (r1 + r2) > r3 or (r1 + r3) > r2 or (r2 + r3) > r1:
    if r1 == r2 == r3:
        print(f"Este triângulo é Equilátero pois seus 3 lados são iguais.")

    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Este triângulo é Isóseles pois apenas 2 lados são iguais")

    else:
        print("Este triângulo é Escaleno pois nenhum lado é igual")
        
    print("É possivel formar um triangulo")

else:
    print("Não é possivel formar um triangulo")