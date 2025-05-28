#aumentar(), diminuir(), dobro() e metade()

def aumentar(preco, porcento):
    preco = preco + (preco * (porcento/100))
    return preco


def diminuir(preco, porcento):
    preco = preco - (preco * (porcento/100))
    return preco


def dobro(preco):
    preco *= 2
    return preco


def metade(preco):
    preco /= 2
    return preco