
# crie um programa onde o usuário digite uma expressão qualquer que use parênteses
# seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fachados na ordem correta

expressao = str(input("Digite a expressão: ")).replace(" ", "")

parenteses = []

for p in expressao:
    parenteses.append(p)


if parenteses.count('(') == parenteses.count(')'):
    print("Expressão valida")

else:
    print("Expressão invalidada")
