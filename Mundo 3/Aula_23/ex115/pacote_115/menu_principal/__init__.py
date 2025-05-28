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


def linha(tam=30):
    return '-' * tam


def cabecalho(texto):

    print(linha())
    print(texto.center(30))
    print(linha())


def menu(lista):

    cabecalho("MENU PRINCIPAL")
    i = 1
    for item in lista:
        print(f"{i} - {item}")
        i += 1
    print(linha()) 
    opcao = leiaInt("Sua opção: ")
    return opcao