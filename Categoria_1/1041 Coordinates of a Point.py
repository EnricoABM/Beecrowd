x, y = map(float, input().split())

Q1 = x > 0 and y > 0
Q2 = x < 0 and y > 0
Q3 = x < 0 and y < 0
Q4 = x > 0 and y < 0
O = x == 0 and y == 0
X = y == 0
Y = x == 0

if Q1:
    print('Q1')
elif Q2:
    print('Q2')
elif Q3:
    print('Q3')
elif Q4:
    print('Q4')
elif O:
    print('Origem')
elif X:
    print('Eixo X')
elif Y:
    print('Eixo Y')

