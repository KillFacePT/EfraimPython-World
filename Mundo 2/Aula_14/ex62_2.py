
# melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos
# o programa encerra quando ele disser que quer mostar 0 termos


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

# Parte 1 
contagem = 1

while contagem <= 10:

    print(f"{primeiro_termo}", end=" -> ")
    primeiro_termo += razao

    contagem += 1 

print("Fim")

################################
# Parte 2 

contagem = 1
total = 0
mais = 10  # número de termos que começa o programa 

while mais != 0:
    total = total + mais
    while contagem <= total: # vira o numero da contagem de termos 

        print(f"{primeiro_termo}", end=" -> ")
        primeiro_termo += razao

        contagem += 1 
        mais = int(input("Quantos termos você quer mostrar a mais? "))

print(f"Progressão finalizada com {total} termos mostrados")