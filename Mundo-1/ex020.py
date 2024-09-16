"""
    O mesmo professor do desafio anterior quer sortear a ordem de apredentaçao de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e moste a ordem sorteada
"""

from random import shuffle


primeiro_aluno = input("Primeiro aluno: ")
segundo_aluno = input("Segundo aluno: ")
terceiro_aluno = input("Terceiro aluno: ")
quarto_aluno = input("Quarto aluno: ")

lista_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]

shuffle(lista_alunos)

print(f"A ordem de apresentaçao será: {lista_alunos}")
