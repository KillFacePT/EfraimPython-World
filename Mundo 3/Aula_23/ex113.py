

def leiaInt(numero):

    while True:

        try:
            n1 = int(input(numero))

        except (ValueError, TypeError):
            print("Erro. Por favor, digite um número inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário.")
            return 0
        else:
            return n1
        
        
def leiaFloat(numero):
    while True:

        try:
            n1 = float(input(numero))

        except (ValueError, TypeError):
            print("Erro. Por favor, digite um número inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print("Entrada de dados interrompida pelo usuário.")
            return 0
        else:
            return n1


num = leiaInt("Digite um Inteiro: ")
num2 = leiaFloat("Digite um Real: ")

print(f"O valor inteiro é: {num} e o real foi {num2}")