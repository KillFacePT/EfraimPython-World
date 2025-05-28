
# faça um programa que tenha uma função notas() que pode recever várias notas de alunos e vai retornar um dicionário
# com as seguintes informações: 
# quantidade de notas
# a maior nota
# a menor nota 
# a média da turma
# a situação(opcional)

# adicone também as docstrings da função 

def notas(*n, sit=False):

    dicio_notas = {}

    dicio_notas["total"] = len(n)
    dicio_notas['maior'] = max(n)
    dicio_notas['menor'] = min(n)
    dicio_notas['media'] = float((f"{(sum(n) / len(n)):.2f}"))

    if sit == True:
        if dicio_notas['media'] >= 7:
            dicio_notas['situação'] = "BOA"

        elif dicio_notas['media'] > 7 and dicio_notas['situação'] >= 6:
            dicio_notas['situação'] = "MEDIANA"
        
        else:
            dicio_notas['situação'] = "RUIM"

    return dicio_notas

resposta = notas(5.5, 9.5, 10, 6.5, sit=True)

print(resposta)

