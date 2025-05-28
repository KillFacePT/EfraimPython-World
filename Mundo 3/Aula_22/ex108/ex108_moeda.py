

def aumentar(preco=0, porcento=0):
    preco = preco + (preco * (porcento/100))
    return preco


def diminuir(preco=0, porcento=0):
    preco = preco - (preco * (porcento/100))
    return preco


def dobro(preco=0):
    preco *= 2
    return preco


def metade(preco=0):
    preco /= 2
    return preco

def coin(preco = 0, coin="R$ "):
    return f"{coin}{preco:.2f}".replace(".", ",")