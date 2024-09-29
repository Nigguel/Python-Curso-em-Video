"""
    Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condiçao de pagamento:
    
    - A vista dinheiro/cheque: 10% de desconto.
    - A vista no cartao: 5% de desconto.
    - Em até 2x no cartao: preço normal
    - 3x ou mais no cartao: 20% de juros
"""

print("========== LOJA FERNANDEZ ==========")

preco = input("Preço das compras: R$")
preco_float = float(preco)

print(
    "\nFORMAS DE PAGAMENTO\n[ 1 ] a vista dinheiro/cheque\n[ 2 ] a vista cartao\n[ 3 ] 2x no cartao\n[ 4 ] 3x ou mais no cartao"
)

opcion = int(input("\nQual é a opçao?: "))

if opcion == 1:
    desconto = preco_float * 0.10
    preco_final = preco_float - desconto
    print(f"Sua compra de R${preco_float:.2f} vai custar R${preco_final:.2f} no final.")

elif opcion == 2:
    desconto = preco_float * 0.05
    preco_final = preco_float - desconto
    print(f"Sua compra de R${preco_float:.2f} vai custar R${preco_final:.2f} no final.")

elif opcion == 3:
    print(f"O total a pagar é de R${preco_float}")

elif opcion == 4:
    parcelas = int(input("Quantas parcelas?: "))
    juros = preco_float * 0.20
    preco_final = preco_float + juros
    print(
        f"Sua compra será parcelada em {parcelas}x de R${(preco_final/parcelas):.2f} com juros\nSua compra de R${preco_float:.2f} vai custar R${preco_final:.2f} no final"
    )
