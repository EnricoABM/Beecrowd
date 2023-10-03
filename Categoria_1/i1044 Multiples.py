A, B = map(int, input().split())
if A < B:
    if B % A == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao multiplos')
else:
    if A % B == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao multiplos')