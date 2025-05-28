
# crie um peuqueno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
# em um arquivo de texto simples
# o sitema só vai ter 2 opções: cadastrar uma nova pessoa e lista todas as pessoas cadastradas

from pacote_115.menu_principal import *
from pacote_115.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    criarArquivo(arq)

while True: # função dentro da variavel para poder fazer condições
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"]) 

    if resposta == 1:
        # opção de listar o conteúdo de um arquivo
        sleep(0.5)
        lerArquivo(arq)

    elif resposta == 2:
        # opção de cadastrar uma nova pessoa
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: ")).capitalize()
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabecalho("Saindo do sistema")
        break
    
    else:
        print("ERRO! Digite uma opção válida")