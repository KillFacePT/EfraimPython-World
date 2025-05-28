
# Crie um programa que leia duas notas de um aluno e calcule sua média 
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: reprovado
# Média entre 5.0 e 6.9: recuperação
# Média 7.0 ou superior: aprovado 
 
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Média: {media}")
    print("Aprovado")

elif media >= 5 and media <= 6.9:
    print(f"Média: {media}")
    print("Recuperação")

elif media < 5:
    print(f"Média: {media}")
    print("Reprovado")