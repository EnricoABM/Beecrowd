soma = 0.
qntPositivos = 0

for i in range(6):
    valor = float(input())
    if valor > 0:
        soma += valor
        qntPositivos += 1

media = soma/qntPositivos

print(f'{qntPositivos} valores positivos')
print(f'{media:.1f}')
