DDD = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte',
}
N = input()
if DDD.get(int(N)) is None:
    print('DDD nao cadastrado')
else:
    print(DDD[int(N)])
