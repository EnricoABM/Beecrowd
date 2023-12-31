
N = int(input())

ordem = [100, 50, 20, 10, 5, 2, 1]
notas = []

i = 0
aux = N
while i < 7:
    notas.append(aux//ordem[i])
    aux = aux%ordem[i]
    i += 1    

print(N)
j = 0
while j < 7:
    print(f'{notas[j]} nota(s) de R$ {ordem[j]},00')
    j += 1