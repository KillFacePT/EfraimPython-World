
# faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# quando o usuário digitar a palavra "FIM" o programa se encerrará
# OBS: use cores.

from time import sleep

print("-=" * 15)
print(f"{"SISTEMA DE AJUDA PyHELP":^30}")
print("-=" * 15)

def ajudar(funcao):

    help(funcao)

    return help


while True:

    busca = str(input("Função ou Biblioteca: ")).lower()

    if busca == "fim":
        break

    print("-=" * 15)
    print(f"{f"Acessando o manual do comando {busca}":^30}")
    print("-=" * 15)

    sleep(1)
    ajudar(busca)
    print("-=" * 15)

print("Até Logo")