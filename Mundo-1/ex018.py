"""
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import cos, tan, sin, radians


angulo = input("Digite o ângulo que você deseja: ")
angulo_float = float(angulo)

angulo_rad = radians(angulo_float)
seno = sin(angulo_rad)
coseno = cos(angulo_rad)
tangente = tan(angulo_rad)

print(
    f"O ângulo de {angulo_float} tem o SENO de {seno:.2f}\nO ângulo de {angulo_float} tem o COSSENO de {coseno:.2f}\nO ângulo de {angulo_float} tem a TANGENTE de {tangente:.2f}"
)
