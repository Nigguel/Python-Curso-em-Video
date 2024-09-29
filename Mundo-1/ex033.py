"""
    Escreva um programa que pergunte o salário de um funcionario e calcule o valor de sue aumento.
    Para salarios superiores a R$1250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15% , 
"""

salario = input("Qual é o salario do funcionário?: R$")
salario_float = float(salario)

if salario_float > 1250:
    aumento = salario_float * 0.10
else:
    aumento = salario_float * 0.15

salario_novo = salario_float + aumento

print(f"Quem ganhava R${salario_float:.2f} passa a ganhar R${salario_novo:.2f} agoara.")
