"""
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis sobre ele. 
"""

a = input("Digite algo: ")
print(
    f"O tipo desse valor é {type(a)}\nSó tem espaços? {a.isspace()}\nÉ um número? {a.isnumeric()}\nÉ alfabetico? {a.isalpha()}\nÉ alfanumerico? {a.isalnum()}\nEstá em maiúsculas? {a.isupper()}\nEstá em minúsculas? {a.islower()}\nEstá capitalizada? {a.istitle()}"
)
