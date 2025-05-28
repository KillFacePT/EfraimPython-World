
# modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda()
# desenvolvida no desafio 108

import ex109_moeda

preco = float(input("Digite o preço:R$ "))

print("-=" * 10)

print(f"A metade de {ex109_moeda.coin(preco)} é {ex109_moeda.metade(preco, True)}")
print(f"O dobro de {ex109_moeda.coin(preco)} é {ex109_moeda.dobro(preco, True)}")
print(f"Aumentando 10%, temos {ex109_moeda.aumentar(preco, 10, False)}")
print(f"Reduzindo 13%, temos {ex109_moeda.diminuir(preco, 13, False)}")

