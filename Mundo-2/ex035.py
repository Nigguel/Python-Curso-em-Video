"""
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestaçao mensal, nao pode exceder 30% do salário ou entao o empréstimo será negado.
"""

valor_casa = input("Valor da casa: R$")
valor_casa_float = float(valor_casa)

salario = input("Salario del comprador: R$")
salario_float = float(salario)

anos = input("Quantos anos de financiamento? ")
anos_int = int(anos)

parcela = valor_casa_float / (anos_int * 12)

porcentaje_minimo_aprovacion = salario_float * 0.30

if parcela < porcentaje_minimo_aprovacion:
    print(
        f"Para pagar uma casa de R${valor_casa_float:.2f} em {anos_int} anos a prestaçao será de R${parcela:.2f}\nEmprestimo pode ser concedido"
    )
else:
    print(
        f"Para pagar uma casa de R${valor_casa_float:.2f} em {anos_int} anos a prestaçao será de R${parcela:.2f}\nEmprestimo Negado"
    )
