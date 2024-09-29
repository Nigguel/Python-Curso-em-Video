"""
    Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a base de conversao:
    -1 para binario
    -2 para octal
    -3 para hexadecimal
"""

numero = input("Digite un número inteiro: ")
numero_int = int(numero)

print(
    "Escolha uma das bases para conversao:\n[ 1 ] converter para Binario\n[ 2 ] converter para Octal\n[ 3 ] converter para Hexadeciaml"
)

opcion = input("Sua opcion: ")
opcion_int = int(opcion)

if opcion_int == 1:
    print(f"O numero {numero_int} em Binario é {bin(numero_int)[2:]}")
elif opcion_int == 2:
    print(f"O numero {numero_int} em Octal é {oct(numero_int)[2:]}")
elif opcion_int == 3:
    print(f"O numero {numero_int} em Hexadecimal é {hex(numero_int)[2:]}")
else:
    print("Opcion invalida, por favor intente nuevamente.")
