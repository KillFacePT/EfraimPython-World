
def aumentar(preco=0, porcento=0, formatado = False):
    preco = preco + (preco * (porcento/100))
    if formatado is False:
        return preco
    else:
        return coin(preco)


def diminuir(preco=0, porcento=0, formatado = False):
    preco = preco - (preco * (porcento/100))
    if not formatado : # se não formatado se não(Dizendo que é negativo ou False)
        return preco
    else:
        return coin(preco)


def dobro(preco=0, formatado = False):
    preco *= 2
    if formatado == False:
        return preco
    else:
        return coin(preco)


def metade(preco=0, formatado = False):
    preco /= 2

    if formatado == False:
        return preco
    else:
        return coin(preco)


def coin(preco = 0, coin="R$ "):
    return f"{coin}{preco:.2f}".replace(".", ",")