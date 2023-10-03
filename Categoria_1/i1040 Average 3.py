

N1, N2, N3, N4 = map(float, input().split())

media = ((N1*2) + (N2 * 3) + (N3 * 4) + N4) / 10

print(f'Media: {media:0.1f}')

if media >= 7:
    print('Aluno aprovado.')
elif media >= 5 and media < 7:
    print('Aluno em exame.')
    exame = float(input("Nota do exame: "))
    media = (media + exame)/2
    if media > 5:
        print('\nAluno aprovado.')
    else: 
        print('\nAluno reprovado.')
    print(f'Media Final: {media}')
elif media < 5:
    print('Aluno reprovado.')
