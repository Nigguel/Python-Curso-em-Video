"""
    Faça um programa que leia um número qualquer e mostre o seu factorial.
"""

numero = int(input("Digite um número para calcular seu factorial: "))
c = numero
f = 1

print(f"Calculando {numero}! = ", end="")

while c > 0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1

print(f)
