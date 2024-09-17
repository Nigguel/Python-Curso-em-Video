"""
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pero computador. O programa deverá escrever na tela se o usuario venceu ou perdeu.
"""

from random import randint
from time import sleep

computador = randint(0, 5)

print("-=-" * 20)
print("vou pensar em um número entre 0 e 5. tente adivinhar....")
print("-=-" * 20)

usuario = input("Em que número eu pensei? ")
usuario_int = int(usuario)
print("PROCESSANDO...")
sleep(2)

if computador == usuario_int:
    print("PARABENS! Você conseguiu me vencer!")
else:
    print(f"GANHEI! Eu pensei no número {computador} e nao no {usuario_int}!")
