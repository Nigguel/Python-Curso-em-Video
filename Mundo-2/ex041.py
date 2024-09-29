"""
    Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso que tipo de triângulo será formado:
    
    -Equilatero: Todos os lados iguais
    -Isósceles: dois lados iguais
    -Escaleno: Todos os lados diferentes
"""

print("=-=" * 10)
print("   Analisador de triângulos   ")
print("=-=" * 10)

recta_1 = input("Primeiro segmento: ")
recta_1_float = float(recta_1)

recta_2 = input("Segundo segmento: ")
recta_2_float = float(recta_2)

recta_3 = input("Terceiro segmento: ")
recta_3_float = float(recta_3)

if (
    recta_1_float < recta_2_float + recta_3_float
    and recta_2_float < recta_1_float + recta_3_float
    and recta_3_float < recta_2_float + recta_1_float
):
    if recta_1_float == recta_2_float == recta_3_float:
        print("Os segmentos acima podem formar um triângulo Equilátero")
    elif (
        recta_1_float != recta_2_float
        and recta_1_float != recta_3_float
        and recta_2_float != recta_3_float
    ):
        print("Os segmentos acima podem formar um triângulo Escaleno")
    else:
        print("Os segmentos acima podem formar um triângulo Isósceles")
else:
    print("Os segmentos acima nao podem formar um triângulo")
