"""
    Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

preco = input("Qual é o preço do produto? R$")
preco_float = float(preco)

desconto = preco_float * 0.05
preco_final = preco_float - desconto

print(
    f"O produto que custava R${preco_float}, na promoçao com desconto de 5% vai custar R${preco_final:.2f}"
)
