"""
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    
    - A média de idade do grupo.
    - Qual é o nome do homem mais velho.
    -Quantas mulheres têm mennos de 20 anos.
"""

soma_idade = 0
cont_pessoas = 0
idade_homem = 0
nome_home_velho = ""
cont_mulheres_menos_20 = 0

for i in range(1, 5):
    print(f"\n----- {i}ª PESSOA -----")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).lower()

    soma_idade += idade
    cont_pessoas += 1

    if sexo == "m":
        if idade > idade_homem:
            idade_homem = idade
            nome_home_velho = nome

    if sexo == "f":
        if idade < 20:
            cont_mulheres_menos_20 += 1


media_idade = soma_idade / cont_pessoas

print(
    f"\nA média de idade do grupo é de {media_idade} anos.\nO homem mais velho tem {idade_homem} anos e se chama {nome_home_velho}.\nAo todo sao {cont_mulheres_menos_20} mulheres com menos de 20 anos"
)
