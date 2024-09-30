"""
    Crie um programa que leia dois valores e mostre um menu.
    Seu programa deverá realizar a operaçao solicitada em cada caso.

    [ 1 ] somar.
    [ 2 ] multiplicar.
    [ 3 ] maior.
    [ 4 ] novos números.
    [ 5 ] sair do programa.
"""

primeiro_valor = int(input("Primeiro valor: "))
segundo_valor = int(input("Segundo valor: "))

opcao = 1

while opcao != 5:
    print(
        "   [ 1 ] somar\n   [ 2 ] multiplicar\n   [ 3 ] maior\n   [ 4 ] novos números\n   [ 5 ] sair do programa"
    )

    opcao = int(input(">>>>> Qual é a sua opçao?: "))

    if opcao == 1:
        print(
            f"A soma entre {primeiro_valor} + {segundo_valor} = {primeiro_valor + segundo_valor}\n=============================="
        )
    elif opcao == 2:
        print(
            f"O resultado de {primeiro_valor} x {segundo_valor} = {primeiro_valor * segundo_valor}\n=============================="
        )
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print(
                f"Entre {primeiro_valor} e {segundo_valor} o maior valor é {primeiro_valor}\n=============================="
            )
        else:
            print(
                f"Entre {primeiro_valor} e {segundo_valor} o maior valor é {segundo_valor}\n=============================="
            )
    elif opcao == 4:
        print("Informe os números novamentes")
        primeiro_valor = int(input("Primeiro valor: "))
        segundo_valor = int(input("Segundo valor: "))
        print("====================")
    elif opcao == 5:
        print("Finalizando...\n==============================")
    else:
        print("Opçao inválida. Tente novamente\n==============================")

print("Fim do programa! volte sempre!")
