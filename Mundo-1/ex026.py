"""
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""

nome = input("Digite sue nome completo: ").strip()
nome_separado = nome.split()

print(
    f"Muito prazer em te conhecer!\nSe primeiro nome é {nome_separado[0]}\nSeu último nome é {nome_separado[len(nome_separado)-1]}"
)
