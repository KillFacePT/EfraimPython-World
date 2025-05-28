
# crie um programa que tenha uma função chamda voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
# retornando um valor literal indicando se uma pessoa tem voto, NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições



print("-" * 25)
ano_nasc = int(input("Ano de Nascimento: "))


def voto(ano):

    from datetime import date

    idade = date.today().year - ano

    if idade >= 65:
        print(f"Com {idade} anos: VOTO OPCIONAL")

    # if idade >= 65:
    #     return f"Com {idade} anos: VOTO OPCIONAL"

    elif idade >= 18 and idade <= 64:
        print(f"Com {idade} anos: VOTO OBRIGATORIO")
    
    else:
        print(f"Com {idade} anos: NÃO VOTA")

    return idade


voto(ano_nasc)

