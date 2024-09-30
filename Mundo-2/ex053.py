"""
    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.
"""

from datetime import date

ano_atual = date.today().year
cont_maior_idade = 0
cont_menor_idade = 0

for i in range(1, 8):
    ano_nascimento = int(input(f"Em que ano a {i}ª pessoa nasceu?: "))
    if (ano_atual - ano_nascimento) >= 18:
        cont_maior_idade += 1
    else:
        cont_menor_idade += 1

print(
    f"Ao todo tivemos {cont_maior_idade} pessoas maiores de idade\nE tambem tivemos {cont_menor_idade} pessoas menores de idade"
)
