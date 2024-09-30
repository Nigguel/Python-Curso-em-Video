"""
    Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao.
"""

print("=" * 40)
print("          10 TERMOS DE UMA PA")
print("=" * 40)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
decimo = primeiro_termo + 9 * razao

for i in range(primeiro_termo, decimo + razao, razao):
    print(f"{i} -> ", end="")

print("Acabou")
