"""
    Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    - O primeiro valor é maior.
    - O segundo valor é maior.
    - Nao exite valor maior, os dois sao iguais
"""

primeiro_valor = input("Primeiro número: ")
segundo_valor = input("Segundo número: ")

primeiro_valor_float = float(primeiro_valor)
segundo_valor_float = float(segundo_valor)

if primeiro_valor_float > segundo_valor_float:
    print("O primeiro valor é maior")
elif segundo_valor_float > primeiro_valor_float:
    print("O segundo valor é maior")
else:
    print("Os números digitados sao iguas")
