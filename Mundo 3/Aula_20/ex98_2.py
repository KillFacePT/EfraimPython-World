
from time import sleep

def contador(i, f, s):
    
    if s < 0:
        s *= -1

    if s == 0:
        s = 1
        
    print("-=" * 20)
    print(f"Contagem de {i} até {f} de {s} em {s}")
    if i < f:
        contador = i
        while contador <= f:
            print(f"{contador} ", end='', flush=True)
            sleep(0.5)
            contador += s
        print("FIM")
    
    else:
        contador = i
        while contador >= f:
            print(f"{contador} ", end="", flush=True)
            contador -= s
        print("FIM")

contador(1, 10, 1)
contador(10, 0, 2)
print("-=" * 20)
print("Agora é sua vez de personalizar a contagem!")

inicio = int(input("Inicio do contador: "))
fim = int(input("Fim do contador: "))
step = int(input("Passo do contador: "))




contador(inicio, fim, step)