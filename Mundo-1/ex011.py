"""
    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
"""

largura = input("Largura da parede: ")
largura_float = float(largura)
altura = input("Altura da parede: ")
altura_float = float(altura)

area = largura_float * altura_float
tinta = area / 2

print(
    f"Sua parede tem uma dimensao de {largura_float}x{altura_float} e sua área é de {area}m².\nPara pintar essa parede, você precisará de {tinta}L de tinta"
)
