
# crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do python
# só que fazendo a validação para aceitar apenas um valor númerico

# ex: n = leiaInt("Digite um n")

def leiaInt(numero):

    while True:

        n = str(input(numero))

        if n.isnumeric():
            return n # returno funciona como break 

        else:
            print("ERRO! Digite um número inteiro válido.")

num = leiaInt("Digite um n: ")
print(f"Você digitou o número: {num}")