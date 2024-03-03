def verificar(N):
    for i in range(len(N) - 1):
        if N[i] == '1':
            if N[i + 1] == '3':
                return f'{N} es de Mala Suerte'
    return f'{N} NO es de Mala Suerte'


N = input()
print(verificar(N))
