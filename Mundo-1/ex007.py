"""
    Desenvolva em programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

primeira_nota = input("Primeira nota do aluno: ")
primeira_nota_float = float(primeira_nota)
segunda_nota = input("Segunda nota do aluno: ")
segunda_nota_float = float(segunda_nota)

media = (primeira_nota_float + segunda_nota_float) / 2

print(
    f"A média entre {primeira_nota_float} e {segunda_nota_float} é igual a {media:.1f}"
)
