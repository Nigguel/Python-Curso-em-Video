"""
    Faça um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra "A"
    - Em que posiçao ela aparece a primeira vez.
    - Em que posiçao ela aparece a última vez.
"""

frase = input('Escriba uma frase: ').lower()

print(f'A letra A aparece {frase.count('a')} vezes na frase.')
print(f'A primeira letra A aparece na posiçao {frase.find('a') + 1}')
print(f'A ultima letra A aparece na posiçao {frase.rfind('a') + 1}')
