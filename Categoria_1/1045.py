"""
Leia 3 números duplos (A, B e C) que representam os lados de um triângulo e organize-os em ordem decrescente, de modo que o lado A seja o maior dos três lados. A seguir, determine o tipo de triângulo que eles podem fazer, com base nos seguintes casos, sempre escrevendo uma mensagem apropriada:
se A ≥ B + C, escreva a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, escreva a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, escreva a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, escreva a mensagem: TRIANGULO ACUTANGULO
se os três lados forem do mesmo tamanho, escreva a mensagem: TRIANGULO EQUILATERO
se apenas dois lados forem iguais e o terceiro for diferente, escreva a mensagem: TRIANGULO ISOSCELES
Entrada
A entrada contém três números duplos, A (0 <A), B (0 <B) e C (0 <C).

Saída
Imprima todas as classificações do triângulo apresentadas na entrada.
"""

A, B, C = map(float, input().split())
if not B + C >= A:
    print('NAO FORMA TRIANGULO')
else:
    if (A**2) == (B**2 + C**2):
        print('TRIANGULO RETANGULO')
    if (A**2) < (B**2 + C**2):
        print('TRIANGULO OBTUSANGULO')
    if (A**2) > (B**2 + C**2):
        print('TRIANGULO ACUTANGULO')
    if A == B and B == C:
        print('TRIANGULO EQUILATERO')
    if A == B or C == A or B == C:
        print('TRIANGULO ISOSCELES')