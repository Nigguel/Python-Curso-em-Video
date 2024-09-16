"""
    Escreva um programa que converta uma temperatura digitada em °C e converta para °F
"""

c = input("Informe a temperatura em °C: ")
c_float = float(c)

f = (c_float * 1.8) + 32

print(f"A temperatura de {c_float}°C corresponde a {f}°F")
