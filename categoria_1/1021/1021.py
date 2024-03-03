N = float(input())

ordem = [
    10000,
    5000,
    2000,
    1000,
    500,
    200,
    100,
    50,
    25,
    10,
    5,
    1
]

notas = []

i = 0
aux = N * 100
while i < len(ordem):
    notas.append(aux//ordem[i])
    aux = aux % ordem[i]
    i += 1

print('NOTAS:')
j = 0
t = 'nota(s)'
while j < len(ordem):
    if j == 6:
        print('MOEDAS:')
        t = 'moeda(s)'
    print(f'{notas[j]:.0f} {t} de R$ {ordem[j]/100:.2f}')
    j += 1
