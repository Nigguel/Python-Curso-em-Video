"""
    Faça um programa que calcule a soma entre todos os números impares que sao multiplos de três e que se encontram no intervalo de 1 ate 500
"""

soma = 0
cont = 0

for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
        cont += 1

print(f"A soma de todos os {cont} valores solicitados é {soma}")
