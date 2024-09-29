"""
    Faça um programa que leia três números e mostre qual é o maior e qual é o menor
"""

primer_valor = input("Primeiro valor: ")
Primer_valor_int = int(primer_valor)

segundo_valor = input("Segundo valor: ")
segundo_valor_int = int(segundo_valor)

tercer_valor = input("Terceiro valor: ")
tercer_valor_int = int(tercer_valor)

menor = maior = Primer_valor_int

if segundo_valor_int < menor:
    menor = segundo_valor_int

if tercer_valor_int < menor:
    menor = tercer_valor

if segundo_valor_int > maior:
    maior = segundo_valor_int

if tercer_valor_int > maior:
    maior = tercer_valor


print(f"O menor valor digitado foi: {menor}\nO maior valor digitado foi: {maior}")
