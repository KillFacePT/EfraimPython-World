print("-" * 40)
print(f"{"SEQUÊNCIA FIBONACCI":^40}")
print("-" * 40)

termos = int(input("Quantos termos você quer mostrar: ")) # número para posição 

n = 0
count = 0

while count < termos:
    
    fib = (((1 + (5)**0.5) /2)**n - ((1 - (5)**0.5) /2)**n) / 5 ** 0.5

    print(f"{int(fib)}", end=" -> ")

    n += 1

    count += 1    

print("FIM")