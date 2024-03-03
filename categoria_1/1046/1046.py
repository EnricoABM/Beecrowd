H1, H2 = map(int, input().split())
duracao = 24 - abs(H1 - H2) if H1 > H2 else 24 if H1 == H2 else abs(H1 - H2)
print(f'O JOGO DUROU {duracao} HORA(S)')
