
# crie um programa que leia a idade e o sexo de várias pessoas
# a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar
# no final mostre
# a) quantas pessoas tem mais de 18 anos
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20

sexo_masc = 0
sexo_femi = 0
pessoa18 = 0

while True:

    print("=" * 30)
    print(f"{"CADASTRE UMA PESSOA":^30}")
    print("=" * 30)

    idade = int(input("Quantos anos tem? "))
    
    sexo = " "
    while sexo not in "MmFf":

        sexo = str(input("Qual o seu sexo? [M/F] ")).strip().lower()[0]
    
    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("Quer continuar? [S/N] ")).strip().lower()[0]

    if idade > 18:
        pessoa18 +=1

    if sexo == "m":
        sexo_masc += 1

    if sexo == "f" and idade < 20:
        sexo_femi += 1

    if continuar == "n":
        break

print("=" * 30)
print(f"{"FIM DO PROGRAMA":^30}")
print("=" * 30)
print(f"Total de pessoa com mais de 18 anos: {pessoa18}")
print(f"Ao todos temos {sexo_masc} homens cadastrados")
print(f"E temos {sexo_femi} mulher com menos de 20 anos")