"""
    Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
"""

numero = input("Me diga um número qualquer: ")
numero_int = int(numero)

if numero_int % 2 == 0:
    print(f"El número {numero_int} é PAR")
else:
    print(f"El número {numero_int} é ÍMPAR")
