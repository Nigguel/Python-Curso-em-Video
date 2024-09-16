"""
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    
    - O nome com todas as letras maiúsculas e minúsculas.
    - Quantas letras ao todo (sem considerar espaços).
    - Quantas letras tem o primeiro nome
"""


from time import sleep

nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
sleep(2)

separa = nome.split()

print(
    f'Seu nome em maiúsculas é {nome.upper()}\nSeu nome em minúsculas é {nome.lower()}\nSeu nome tem ao todo {len(nome) - nome.count(' ')} letras\nSeu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.'
)
