
# desenvolva um programa que leia o primeiro termo e a razão de uma Progressao Aritimética
# no final, mostre os 10 primeiros termos dessa progressão

# an = ultimo termo
# a1 = primeiro termo
# an = a1 + (n - 1) * r
# n = numero de termos

print("=" * 30)
print(f"{"10 TERMOS DE UMA PA":^30}")
print("=" * 30)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
decimo = primeiro_termo + (10 - 1) * razao # an = a1 + (n - 1) * r

# usando o primeiro termo como inicio do range 
# decimo para os 10 primeiros termos
#razao como step
# decimo + razao porque o python vai até o index 9 então para ir para o decimo foi somado mais a razao

for c in range(primeiro_termo, decimo + razao, razao):
    print(c, end=",")