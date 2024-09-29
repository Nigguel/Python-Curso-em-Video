""" 
    Crie um programa que faça o computador jogar jokenpô com você.
"""

from random import randint


print("Suas opçoes: \n[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] Tesoura")

computador = randint(1, 3)
opcoes = ["PEDRA", "PAPEL", "TESOURA"]

escolha = int(input("Qual é a sua jogada?: "))
print("JO\nKEN\nPO!!!")

print("=-=" * 8)
print(f"Computador jogou {opcoes[computador - 1]}")
print(f"Jogador jogou {opcoes[escolha - 1]}")
print("=-=" * 8)

if computador == 1:  # computador jugou pedra
    if escolha == 1:
        print("Empate")
    elif escolha == 2:
        print("jogador vence")
    else:
        print("Computador vence")

if computador == 2:  # computador jugou papel
    if escolha == 1:
        print("computador vence")
    elif escolha == 2:
        print("empate")
    else:
        print("jogador vence")

if computador == 3:  # computador jugou tesoura
    if escolha == 1:
        print("jogador vence")
    elif escolha == 2:
        print("computador vence")
    else:
        print("empate")
