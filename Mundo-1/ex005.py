"""
    Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

numero = input("Digite um número: ")
numero_int = int(numero)
sucessor = numero_int + 1
antecessor = numero_int - 1

print(
    f"Analisando o valor {numero_int}, seu antecessor é {antecessor} e o sucessor é {sucessor}"
)
