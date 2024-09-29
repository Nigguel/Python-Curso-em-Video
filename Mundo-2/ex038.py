"""
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou sejá passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do do prazo.
"""

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Ano de nascimento: "))
idade = ano_atual - ano_nascimento

if idade < 18:
    print(
        f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.\nAinda faltam {18-idade} anos para o alistamento\nSeu alistamento será em {ano_atual + (18-idade)}"
    )
elif idade > 18:
    print(
        f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.\nVocê ja deveria ter se alistado há {idade - 18} anos\nSeu alistamento foi em {ano_atual - (idade - 18)}"
    )
else:
    print(
        f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.\nVocê tem que se alistar IMEDIATEMENTE!"
    )
