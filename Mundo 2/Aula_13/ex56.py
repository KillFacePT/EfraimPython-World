
# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
# no final do programa mostre:
# a media de idade do grupo
# homem mais velho
# quantas mulheres tem menos de 20 anos

somaidade = 0
media = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
quantidade_mulher = 0

for i in range(1, 5):
    print(f'-----{i}ª Pessoa -----')
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M] ou [F]: ")).lower().strip()
    print(" ")

    somaidade += idade
    media = somaidade / 4


    # if i == 1 and sexo in "Mm": tanto m maiusculo quanto minusculo 
    if sexo == 'm' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome


    if sexo == 'f' and idade < 20:
        quantidade_mulher += 1 

    

print(f"A média de idade é de {media /4} anos")
print(" ")
print(f"O homem mais velho é {nome_homem_mais_velho} com {idade_homem_mais_velho} anos")
print(" ")
print(f"Existem {quantidade_mulher} mulher com menos de 20 anos")
