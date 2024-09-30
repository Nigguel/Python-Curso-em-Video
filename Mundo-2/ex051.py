"""
    Faça um programa que leia um número inteiro e diga se ele é ou nao um número primo.
"""

numero = int(input("Digite um número: "))
cont = 0

for i in range(1, numero + 1):
    print(i, end=" ")
    if numero % i == 0:
        cont += 1

print(f"\nO número {numero} foi divisivel {cont} vezes")

if cont == 2:
    print(f"E por isso ele é primo")
else:
    print(f"E por isso ele nao é primo")
