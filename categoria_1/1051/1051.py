salario = float(input())

aux1 = 0.0
aux2 = 0.0
aux3 = 0.0

if salario > 2000:
    if salario > 3000:
        aux1 = 1000
        if salario > 4500:
            aux2 = 1500
            aux3 = salario - 4500
        else:
            aux2 = salario - 3000
    else:
        aux1 = salario - 2000
    taxa = aux1 * 8/100 + aux2 * 18/100 + aux3 * 28/100
    print(f'R$ {taxa:.2f}')
else:
    print('Isento')
