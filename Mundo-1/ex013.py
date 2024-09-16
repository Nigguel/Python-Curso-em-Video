"""
    Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
"""

salario = input("Qual é o salário do funcionário? R$")
salario_float = float(salario)

aumento = salario_float * 0.15
salario_novo = salario_float + aumento

print(
    f"Um funcionário que ganhava R${salario_float}, com 15% de aumento, passa a receber R${salario_novo:.2f}"
)
