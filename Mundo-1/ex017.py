"""
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e moste o comprimento da hipotenusa.
"""

from math import pow, sqrt


co = input("Comprimento do cateto oposto: ")
co_float = float(co)
ca = input("Comprimento do cateto adjacente: ")
ca_float = float(ca)

hipotenusa = sqrt(pow(co_float, 2) + pow(ca_float, 2))

print(f"A hipotenusa vai medir {hipotenusa:.2f}")
