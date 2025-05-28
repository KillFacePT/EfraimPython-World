
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

    if sair in "n":
        break

#print(chamada[0][1])
print("-=" * 15)
print(f"{"No.":<4}{"NOME":>10}{"Média":>8}")
print("-" * 30)

#print(chamada[0][1][0])

for i, m in enumerate(chamada):
    nome = m[0] # Usar m[0] para acessar o nome do aluno
    notas = m[1]
    media = (m[1][0] + m[1][1]) / 2 

    print(f"{i:<4} {nome:>10} {media:8}")

print("-" * 30)

# ENUMERATE() 
# enumerei a lista chamada onde o index zero recebe o primeiro aluno adicionado
# primeira posição o index zero é o nome e index 1 as notas 
# a primeira nota index zero e segunda nota index 1 