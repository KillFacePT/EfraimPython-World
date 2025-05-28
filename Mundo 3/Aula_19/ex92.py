
# crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionatio
# se por acaso o CTPS for diferente de Zero, o dicionário receberá também o ano de contratação e o salário
# calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
# 35 anos de carteira assinada

from datetime import date 
pessoa = {}

pessoa['nome'] = str(input("Nome: "))

ano_nasc = int(input("Ano Nascimento: "))
pessoa['idade'] = date.today().year - ano_nasc

ct = int(input("Carteira de trabalho (0 não tem): "))

if ct > 0:
    pessoa['CTPS'] = ct
    pessoa['contratação'] = int(input("Ano de contratação: "))
    pessoa['salario'] = float(input("R$: "))
    pessoa['aposentadoria'] = (pessoa['contratação'] - ano_nasc) + 35
else:
    pessoa['CTPS'] = "Sem CTPS"

print(pessoa)

for k, v in pessoa.items():
    print(f"{k} tem o valor {v}")
# pessoa = {"nome": str(input("Nome: "))}

