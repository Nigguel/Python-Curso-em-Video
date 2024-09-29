"""
    Faça um programa que leia um ano qualquer e mostre se ele é bissexto
"""

from datetime import date

ano = input("Que ano quer analizar? Coloque 0 para analizar o ano atual: ")

ano_int = int(ano)

if ano_int == 0:
    ano_int = date.today().year

if ano_int % 4 == 0 and ano_int % 100 != 0 or ano_int % 4 == 0:
    print(f"O ano {ano_int} é BISSEXTO")
else:
    print(f"O ano {ano_int} nao é BISSEXTO")
