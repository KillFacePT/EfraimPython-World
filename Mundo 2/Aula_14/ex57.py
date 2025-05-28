
# faça um progrma que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'.
# caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite seu sexo, [M] para masculino e [F] para feminino: ")).upper().strip(" ")[0]

while sexo not in "MmFf":
    
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).upper().strip(" ")[0]

    
if sexo == "M":
    print("Sexo Masculino registrado com sucesso")

elif sexo == "F":
    print("Sexo Feminino registrado com sucesso")
