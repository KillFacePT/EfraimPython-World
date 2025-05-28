
# adapte o código do desafio 107, criando uma função adicional chamada moeda() 
# que consiga mostra os valores como um valor mo monetário formatado
import ex108_moeda

preco = float(input("Digite o preço:R$ "))

print("-=" * 10)

print(f"A metade de {ex108_moeda.coin(preco)} é {ex108_moeda.coin(ex108_moeda.metade(preco))}")
print(f"O dobro de {ex108_moeda.coin(preco)} é {ex108_moeda.coin(ex108_moeda.dobro(preco))}")
print(f"Aumentando 10%, temos {ex108_moeda.coin(ex108_moeda.aumentar(preco), 10)}")
print(f"Reduzindo 13%, temos {ex108_moeda.coin(ex108_moeda.diminuir(preco), 13)}")