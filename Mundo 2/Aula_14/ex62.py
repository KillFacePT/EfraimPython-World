
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


while primeiro_termo < (enesimo + razao): 
    
    print(f"{primeiro_termo}", end=" -> ")

    primeiro_termo += razao
print("Pausa")
 

termos = 10 # simula que o usuário digitou 10 termos, número de termos que começa o programa 
total = 0 # total de termos que vai ser printado na tela 

while termos != 0: 
    total = total + termos # total a ser mostrado vai ser total = 0 + quantidade de termos que o usuária quer a mais 

    termos =int(input("Quantos termos você quer mostar a mais? "))
    

    if termos != 0:
        
        sair = termos

        while sair != 0:

            enesimo += razao
            print(f"{enesimo}", end=" -> ")
                
            sair -= 1
        print("Pausa")

   
print(f"Progressão finalizada com {total} termos mostrados")
