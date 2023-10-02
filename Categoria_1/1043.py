
A, B, C = map(float, input().split())

triangulo = B + C > A and A + B > C and A + C > B


if triangulo:
    print(f'Perímetro: {A + B + C}')
else:
    print(f'Área: {((A + B)*C)/2}')
"""
6 4 2
True
6 4 2.1
False
"""