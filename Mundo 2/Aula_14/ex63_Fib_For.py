
n = int(input("Digite um número: ")) # número para posição 

f = 0

for i in range(0, n):
    
    fib = (((1 + (5)**0.5) /2)**f - ((1 - (5)**0.5) /2)**f) / 5 ** 0.5

    print(f"{int(fib)}", end=" -> ")

    f += 1 

print("FIM")