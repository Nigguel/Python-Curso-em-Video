"""
    Refaça o DESAFIO 009, mostrando a tabuada de um número que o usário escolher, só que agora utilizando um laço for.
"""

numero = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i:2} = {numero*i}")
