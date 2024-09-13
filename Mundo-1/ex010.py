"""
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
    
    considere US$1.00 = R$3.27
"""

dinheiro = input("Quanto dinheiro você tem na carteira?: R$")
dinheiro_float = float(dinheiro)
dolar = dinheiro_float / 3.27

print(f"Com R${dinheiro_float} você pode comprar US${dolar:.2f}")
