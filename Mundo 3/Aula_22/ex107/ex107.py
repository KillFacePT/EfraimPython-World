
# crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()
# faça também um programa que importe esse módulo e use algumas dessas funções 

import ex107_moeda
preco = float(input("Digite o preço:R$ "))

print("-=" * 10)

print(f"A metade de {preco} é {ex107_moeda.metade(preco):.2f}")
print(f"O dobro de {preco} é {ex107_moeda.dobro(preco):.2f}")
print(f"Aumentando 10%, temos {ex107_moeda.aumentar(preco, 10):.2f}")
print(f"Reduzindo 13%, temos {ex107_moeda.diminuir(preco, 13):.2f}")