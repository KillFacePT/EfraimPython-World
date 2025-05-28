
from utilidadescev import moeda
from utilidadescev import dados

preco = dados.leiaDinheiro("Digite um preço: R$ ")
moeda.resumo(preco, 35, 22)