valores = map(float, input().split())
A, B, C = sorted(list(valores), reverse=True)

tri = A >= B + C
tri_ren = A**2 == B**2 + C**2
tri_obt = A**2 > B**2 + C**2
tri_acu = A**2 < B**2 + C**2
tri_equ = A == B and A == C and B == C
tri_iso = A == B or A == C or B == C

if tri:
    print('NAO FORMA TRIANGULO')
else:
    if tri_ren:
        print('TRIANGULO RETANGULO')
    if tri_obt:
        print('TRIANGULO OBTUSANGULO')
    if tri_acu:
        print('TRIANGULO ACUTANGULO')
    if tri_equ:
        print('TRIANGULO EQUILATERO')
    elif tri_iso:
        print('TRIANGULO ISOSCELES')
