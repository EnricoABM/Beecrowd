def entrada(M, lista):
    i = 0
    while i < M:
        # Vi (1 ≤ Vi ≤ 500)
        V_valor_moeda = int(input())
        lista.append(V_valor_moeda)
        i += 1


def somar_valores(N, lista):
    j = 0
    soma = 0
    while j < len(lista):
        soma += lista[j]
        j += N
    return soma


def verificar_primo(soma):
    k = 1
    l = 0
    while k <= soma:
        if soma % k == 0:
            l += 1
        k += 1
    if l == 2:
        return True
    return False


while True:
    moedas: list[int] = []

    # M (2 ≤ M ≤ 20)
    M_qntd_moedas = int(input())
    entrada(M_qntd_moedas, moedas)

    # N (1 ≤ N ≤ M)
    N_pulos = int(input())
    soma_valores = somar_valores(N_pulos, moedas)

    if not verificar_primo(soma_valores):
        print('Bad boy! I’ll hit you.')
    else:
        print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        break
