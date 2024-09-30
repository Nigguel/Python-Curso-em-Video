"""
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitaçao novamente até ter um valor correto.
"""

sexo = str(input("Informe seu sexo: [M/F] ")).upper().strip()

while sexo not in "MF":
    print("Dados inválidos. Poor favor, informe seu sexo")
    sexo = str(input("Informe seu sexo: [M/F] ")).upper()

print(f"Sexo {sexo} registrado com sucesso")
