
# faça um programa que mostre a tabuada de vários números
# um de cada vez, para cada valor digitado pelo usuário
# o programa será interrompido quando o número solicitado for negativo


while True:

    num = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 20)
    
    if num < 0:
        break

    else:
        for i in range(1, 11):

            multi = num * i
            print(f"{num} x {i} = {multi}")

        print("-" * 20)

print("Programa TABUADA encerrado")