"""
    Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
    - Média abaixo de 5.0: REPROVADO
    - Média entre 5.0 e 6.9: RECUPERAçAO
    - Média 7.0 ou superior: APROVADO
"""

primeira_nota = input("Primeira nota: ")
segunda_nota = input("Segunda nota: ")

primeira_nota_float = float(primeira_nota)
segunda_nota_float = float(segunda_nota)

media = (primeira_nota_float + segunda_nota_float) / 2

print(
    f"tirando {primeira_nota_float:.1f} e {segunda_nota_float:.1f}, a média do aluno é {media:.1f}"
)

if media >= 7:
    print("O aluno está APROVADO.")
elif media < 5:
    print("O aluno está REPROVADO")
else:
    print("O aluno está em RECUPERAçAO")
