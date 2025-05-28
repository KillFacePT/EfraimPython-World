
# faça um programa que leia nome e média de um aluno, guardando também a situação em um dicit()
# no final mostre o conteúdo da estrutura na tela

aluno = {}
sala = []

while True:
    
    aluno['aluno'] = str(input("Nome: ")).upper()
    aluno['media'] = float(input("Média: "))
    sair = str(input("Sair: [S/N] ")).lower()

    sala.append(aluno.copy())
    aluno.clear()

    if sair in "s":
        break

for s in sala:

    print(f"O aluno [{s['aluno']}], tem média de: {s['media']}")

    
    if s['media'] >= 7:
        print("Situação é igual Aprovado")

    else:
        print("Situação igual a Reprovado")
    
    

    