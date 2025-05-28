
expre = str(input("Digite a expressão: "))

pilha = []

for simbulo in expre: 
    if simbulo == "(": # se o simbulo for "(" adicione a lista pilha
        pilha.append("(")

    elif simbulo == ")": # senão se simbulo for ")"
        if len(pilha) > 0: # se o tamanho da lista for maior que zero .pop() deleta o ultimo elemento da lista (que seria o parenteses aberto)
            pilha.pop()
        
        else:
            pilha.append(")") # sinal que teve mais parenteses fechando do que abrindo 
            break

if len(pilha) == 0:
    print("Sua expressão é valida")

else:
    print("Sua expressão é invalida")

# pra cada parenteses aberto quando um parenteses fechar ele vai apagar o ultimo aberto fazendo que nao tenha nenhum parenteses na lista
# confirmando a condicao de len(pilha) == 0 
# se um parenteses aberto for adicionado o proximo primeiro parenteses de fechamendo vai excluir o parenteses aberto fazendo um par de parenteses 