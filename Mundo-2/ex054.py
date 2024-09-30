"""
    Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi e mior e o menor peso lidos.
"""

maior = menor = 0

for i in range(1, 6):
    peso = float(input(f"Peso da {i}ª pessoa: "))
    if i == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso lido foi de {maior}Kg\nO menor peso lido foi de {menor}Kg.")
