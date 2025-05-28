
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# seno, cosseno e tangente desse ângulo 
import math

angulo = float(input("Digite o ângulo: "))


print(f"O seno do ângulo de {angulo} é: {(math.sin(math.radians(angulo)))}")
print(f"O cosseno do ângulo de {angulo} é: {(math.cos(math.radians(angulo)))}")
print(f"A tangente do ângulo de {angulo} é: {(math.tan(math.radians(angulo)))}")

