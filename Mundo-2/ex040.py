"""
    A cofederaçao Nacional de Nataçao precisa de um programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade:
    
    - Até 9 anos: MIRIM
    - Até 14 anos: INFANTIL
    - Até 19 anos: JUNIOR
    - Até 25 anos: SÊNIOR
    - Acima: MASTER
"""

from datetime import date


ano_nascimento = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"O atleta tem {idade} anos.")

if idade <= 9:
    print("Classificaçao: MIRIM")
elif 9 < idade <= 14:
    print("Classificaçao: INFANTIL")
elif 14 < idade <= 19:
    print("Classificaçao: JUNIOR")
elif 19 < idade <= 25:
    print("Classificaçao: SENIOR")
else:
    print("Classificaçao: MASTER")
