"""
    Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.
"""

from random import randint

cont = 1

computador = randint(0, 11)
print(
    "Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?"
)
palpite = int(input("Qual é seu palpite?: "))

while palpite != computador:
    if palpite < computador:
        print("Mais... Tente mais uma vez.")

    if palpite > computador:
        print("Menos... Tente mais uma vez.")

    palpite = int(input("Qual é seu palpite?: "))
    cont += 1

print(f"Acertou com {cont} tentativas. Parabens!")
