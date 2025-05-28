
# crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# no final, mostre a matriz na tela, com a formatação correta


matriz = [[], [], []]


for l in range(0, 3):

    for c in range(0, 3):
        matriz[l].append(int(input(f"Digite um valor para [{l}, {c}]: ")))    

print("-=" * 30)
# imprimir a matriz 
# Lista em L
#      0          1          2
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Lista em C
#   0  1  2    0  1  2    0   1  2
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


for l in range(0, 3):

    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")

        # vai comecar o print no L-0 e vai entrar no segundo for de C 
        # vai imprimir toda a lista do index 0 em L e suas posições 
        # depois vai para o proximo range e assim por diante 
    
    print()
