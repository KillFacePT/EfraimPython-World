
# faça um programa que leia nome e média de um aluno, guardando também a situação em um dicit()
# no final mostre o conteúdo da estrutura na tela

aluno = {}

nome = str(input("Nome: ")).upper()
media = float(input("Média: "))

aluno["nome"] = nome
aluno["média"] = media 

print(f"O nome é {aluno['nome']}")
print(f"Média é igual a {aluno["média"]}")

if aluno["média"] >= 7:
    aluno['situação'] = "aprovado"

elif 5<= aluno["média"] < 7:
    aluno['situação'] = "recuperação"

else:
    aluno['situação'] = "reprovado"

print("-" * 15)
print(aluno)
print("-" * 15)

for k, v in aluno.items():
    print(f"{k} é {v}")