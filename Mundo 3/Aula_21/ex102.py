
# crie um programa que tenha uma função fatorial()
# que receba dois parametros:
# o primeiros que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial 

numero = int(input("Fatorial de qual número: "))
mostrar = str(input("Deseja mostra a conta? [S/N]: ")).lower()[0]

if mostrar == 's':
        mostrar = True

def fatorial(n, show=False):

    fact = 1         
    
    for i in range(n, 0, -1):

        fact *= i

        if show == True:
            print(f"{i}", end="")
            print(" x " if i > 1 else " = ", end="")
    

    return f"{fact}"
    
print("-" * 25)
print(fatorial(numero, mostrar))