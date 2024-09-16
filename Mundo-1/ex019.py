"""
    Um professor quer sortear um dos seus quatro alunos para apagar o quadroo. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""

from random import choice


primeiro_aluno = input("Primeiro aluno: ")
segundo_aluno = input("Segundo aluno: ")
terceiro_aluno = input("Terceiro aluno: ")
quarto_aluno = input("Quarto aluno: ")

lista_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]

escolha = choice(lista_alunos)

print(f"O aluno escolhido foi {escolha}")
