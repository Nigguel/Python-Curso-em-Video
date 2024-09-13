"""
    Escreva um programa que leia um valor em metros e o exiba convertido en centimetros e milimetros
"""

distancia = input("Uma distância em metros: ")
distancia_float = float(distancia)
distancia_cm = distancia_float * 100
distancia_mm = distancia_float * 1000


print(
    f"A medida de {distancia_float}m corresponde a:\n {distancia_cm:.0f}cm\n {distancia_mm:.0f}mm"
)
