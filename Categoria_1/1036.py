"""
Read 3 floating-point numbers. After, print the roots of bhaskara's formula. If it's impossible to calculate the roots because a division by zero 
or a square root of a negative number, presents the message \"Impossivel calcular\".

Input
Read 3 floating-point numbers (double) A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.
"""
A, B, C = map(float, input().split())

delta = (B**2) - (4*A*C)

if delta <= 0 or A == 0:
    print('Impossivel calcular')
 
else:
    R1 = ((B*-1) + (delta**0.5))/(2*A)
    R2 = ((B*-1) - (delta**0.5))/(2*A)
    print(f'R1 = {R1:0.5f}')
    print(f'R2 = {R2:0.5f}')