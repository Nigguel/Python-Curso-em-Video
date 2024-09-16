"""
    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado
"""

dias = input("Quantos dias alugados? ")
km = input("Quantos Km rodados? ")

dias_int = int(dias)
km_float = float(km)

pago_dias = dias_int * 60
pago_km = km_float * 0.15

pago_total = pago_dias + pago_km

print(f"O total a pagar é de R${pago_total:.2f}")
