"""
    Escreva um programa que leia a velocidade de um carro. 
    Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa va custar R$7.00 por cada km acima do limite.
"""

velocidade = input("Qual é a velocidade atual do carro? ")
velocidade_float = float(velocidade)

if velocidade_float <= 80:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    multa = (velocidade_float - 80) * 7
    print(
        f"MULTADO! Você excedeu o limite permitido que é de 80Km/h Você deve pagar uma multa de R${multa:.2f}!\nTenha um bom! Dirija com segurança"
    )
