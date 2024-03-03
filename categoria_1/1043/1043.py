A, B, C = map(float, input().split())

triangulo = B + C > A and A + B > C and A + C > B

if triangulo:
    print(f'Perimetro = {A + B + C}')
else:
    print(f'Area = {((A + B)*C)/2}')
