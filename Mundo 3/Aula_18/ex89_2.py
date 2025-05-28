

aluno = list()
while True:
    nome = str(input("Aluno: ")).upper()
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    media = (nota_1 + nota_2) / 2
    aluno.append([nome, [nota_1, nota_2], media])

    sair = " "
    sair = str(input("Deseja continuar? [S/N]: ")).lower()[0]

    if sair in "n":
        break

#print(aluno)
# Aluno: efraim
# Nota 1: 10
# Nota 2: 8
# [['EFRAIM', [10.0, 8.0], 9.0]]

print("-=" * 15)
print(f"{"No.":<4}{"NOME":>10}{"Média":>8}")
print("-" * 30)

# enumerate serve para enumerar a lista de aluno
#       0         1         2
# [['EFRAIM', [10.0, 8.0], 9.0]]

for i, a in enumerate(aluno):  

    print(f"{i:<4}{a[0]:<10}{a[2]:>8}") # "i" serve para mostar o numero do aluno e "a" serve para index do nome(a[0]) do aluno e média (a[2])

print("-" * 30)

n = 0
while n != 999:

    n = int(input("Mostrar notas de qual aluno? (999 interrompe): "))

    if n in range(len(aluno)):
        print(f"Notas de {aluno[n][0]} são [{aluno[n][1]}]")
        print("-" * 30)