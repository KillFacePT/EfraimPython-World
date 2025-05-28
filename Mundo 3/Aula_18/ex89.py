
# crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta
# no final mostre, um boletim contendo a média de cada um 
# e permita que o usuário possa mostras as notas de cada aluno individualmente

chamada = [] 
notas = []
dados = []

while True:

    nome = str(input("Aluno: ")).upper()
    dados.append(nome)

    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    notas.append(nota_1)
    notas.append(nota_2)

    dados.append(notas[:])
    chamada.append(dados[:])
    
    dados.clear()
    notas.clear()

    sair = " "
    sair = str(input("Deseja continuar? [S/N]: ")).lower()[0]

    if sair not in "sn":
        sair = str(input("Digite apenas com 'S' ou 'N' [S/N]: ")).lower()[0]
    if sair in "n":
        break

#print(chamada[0][1])
print("-=" * 15)
print(f"{"No.":<4}{"NOME":>10}{"Média":>8}")
print("-" * 30)

#print(chamada[0][1][0])

for m in range(len(chamada)):

    media = (chamada[m][1][0] + chamada[m][1][1]) / 2 # m é o index da lista chamada [1] é o index da lista dos dados do aluno [0] é o index da primeira nota

    print(f"{m:<4} {chamada[m][0]:>10} {media:8}")

print("-" * 30)

n = 0
while n != 999:

    n = int(input("Mostrar notas de qual aluno? (999 interrompe): "))

    if n in range(len(chamada)):
        print(f"Notas de {chamada[n][0]} são [{chamada[n][1]}]")
        print("-" * 30)

print(' ')       
print("FINALIZANDO...")
print("<<< VOLTE SEMPRE >>>")


# aluno_ficha = list()
# nome = str(input("Aluno: ")).upper()
# nota_1 = float(input("Nota 1: "))
# nota_2 = float(input("Nota 2: "))
# aluno.append([nome, [nota1, nota2], media])