
# escreva um programa que leia a velocidade de um carro
# se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# a multa vai custar R$: 7,00 por cada Km acima do limite 

velo = int(input("Qual a velocidade do carro? "))

if velo > 80:
    multa = (velo - 80) * 7 
    print("Você está acima da velocidade permitida que é de 80km/h")
    print(f"Valor da multa é: R$:{multa}")
else:
    print("Velocidade permitida")