"""
    Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

numero = input("Digite um número: ")
numero_int = int(numero)
dobro_numero = 2 * numero_int
triplo_numero = 3 * numero_int
raiz_numero = numero_int ** (1 / 2)

print(
    f"O dobro de {numero_int} vale {dobro_numero}\nO triplo de {numero_int} vale {triplo_numero}\nA raiz cuadrada de {numero_int} é igual a {raiz_numero:.2f}"
)
