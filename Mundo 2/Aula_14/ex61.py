
# refaça o desafio 51, lendo o primeiro termo e a razão de uma PA
# mostrando os 10 primeiros termos da progressão usando a estrutura while

# an = ultimo termo (enésimo termo) an10
# a1 = primeiro termo
# An = a1 + (n - 1) * r
# n = numero de termos (é o mesmo número do an que quero descobrir) 10

print("=" * 30)
print(f"{"10 TERMOS DE UMA PA":^30}")
print("=" * 30)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))

enesimo = primeiro_termo + (10 -1) * razao

while primeiro_termo < (enesimo + razao): # enquanto o primeiro termo for menor que (enesimo + razao), dentro do WHILE ele vai ter uma contagem somando a razão até o primeiro termo ficar igual ao enesimo
    
    print(f"{primeiro_termo}", end=" -> ")

    primeiro_termo += razao

print("Fim")


'''

contagem = 10
while contagem <=10:
    print(f"{primeiro_termo}", end=" -> ")

    primerio_termo += razao
    contagem += 1
'''