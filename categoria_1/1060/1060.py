cont_positivos = 0
for rep in range(6):
    valor = float(input())
    if valor >= 0:
        cont_positivos += 1

print(f'{cont_positivos} valores positivos')
