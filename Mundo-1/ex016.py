"""
    Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porçao inteira.
"""

from math import trunc


numero = input("Digite um valor: ")
numero_float = float(numero)

porcao_inteira = trunc(numero_float)

print(f"O valor digitado foi {numero_float} e a sua porçao inteira é {porcao_inteira}")
