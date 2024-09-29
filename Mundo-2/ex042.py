"""
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
    
    - Abaixo de 18.5: Abaixo do Peso.
    - Entre 18.5 e 25: Peso ideal.
    - 25 até 30: Sobrepeso.
    - 30 até 40: Obesidade.
    - Acima de 40: Obesidade mórbida.
"""

peso = input("Qual é seu peso? (kg) ")
peso_float = float(peso)

altura = input("Qual é a sua altura? (m) ")
altura_float = float(altura)

imc = peso_float / (altura_float**2)

print(f"O IMC dessa pessoa é de {imc:.1f}")

if imc < 18.5:
    print("Você está Abaixo do Peso.")
elif 18.5 <= imc < 25:
    print("Você está em um peso ideal")
elif 25 <= imc < 30:
    print("Você está com sobrepeso")
elif 30 <= imc < 40:
    print("Você está com obesidade")
else:
    print("Você esta com obesidade Morbida")
