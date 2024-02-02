# nome[i] != 'aeiou'

qntd_nomes = int(input())

nomes = [input() for i in range(qntd_nomes)]

desc_nomes = []
for nome in nomes:
    seq = 0
    for letra in nome:
        if letra.lower() not in 'aeiou':
            seq += 1
        else:
            seq = 0
        if seq == 3:
            break
    if seq >= 3:
        desc_nomes.append(f'{nome} nao eh facil')
    else:
        desc_nomes.append(f'{nome} eh facil')

print(*desc_nomes, sep='\n')
