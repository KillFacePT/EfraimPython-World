
# um professor quer sortear um dos seus quatro alunos para apagar o quadro
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

a1 = str(input("Primeiro Aluno: "))
a2 = str(input("Segundo Aluno: "))
a3 = str(input("Terceiro Aluno: "))
a4 = str(input("Quarto Aluno: "))

lista = [a1, a2, a3, a4]

escolhido = random.choice(lista)

print(f"O aluno escolhido foi {escolhido}")