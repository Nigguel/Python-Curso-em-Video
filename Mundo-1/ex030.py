"""
    Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200Km e R$0.45 para viagens mais longas.    
"""

distacia = input("Qual é a distancia da sua viagem? ")
distancia_float = float(distacia)

if distancia_float <= 200:
    preco = distancia_float * 0.50
else:
    preco = distancia_float * 0.45

print(
    f"Você está prestes a começar uma viagem de {distancia_float:.1f}Km.\nE o preço da sua passagem será de R${preco:.2f}"
)
