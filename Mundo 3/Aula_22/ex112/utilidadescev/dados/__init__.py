def leiaDinheiro(mensagem):
    valido = False

    while not valido:
        entrada = str(input(mensagem)).replace(",", ".").strip()

        if entrada.isnumeric():
            valido = True
            return float(entrada)
        
        else:
            print(f"ERRO [{entrada}] é um preço inválido !")