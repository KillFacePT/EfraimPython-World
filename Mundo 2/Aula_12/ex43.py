
# desenvolva uma lógica que leia o peso e a altura de uma pessoa
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# abaixo de 18.5: abaixo do peso 
# entre 18.5 e 25: peso ideal 
# 25 ate 30: sobrepeso
# 30 ate 40: obesidade
# acima de 40: obesidade mórbida

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura **2)

if imc < 18.5:
    print("Abaixo do peso")

# 18.5 <= imc <= 25:
elif imc >= 18.5 and imc <= 25:
    print("Peso ideal")

elif imc > 25 and imc <= 30:
    print("Sobrepeso")

elif imc > 30 and imc <= 40:
    print("Obesidade")

else:
    print("Obesidade mórbida")