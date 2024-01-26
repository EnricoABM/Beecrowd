N = float(input())

ordem = [
    100.00,
    50.00, 
    20.00, 
    10.00, 
    5.00, 
    2.00, 
    1.00, 
    0.5, 
    0.25, 
    0.1, 
    0.05, 
    0.01
]

notas = []

i = 0
aux = N
while i < len(ordem):
    notas.append(aux//ordem[i])
    aux = aux%ordem[i]
    i += 1    

print('NOTAS:')
j = 0
t = 'nota(s)'
while j < len(ordem):
    if j == 6:
        print('MOEDAS:')
        t = 'moeda(s)'
    print(f'{notas[j]:.0f} {t} de R$ {ordem[j]:.2f}')
    j += 1 


