
X, Y = map(int, input().split())

if X == 1:
    res = 4 * Y
elif X == 2:
    res = 4.5 * Y
elif X == 3:
    res = 5 * Y
elif X == 4:
    res = 2 * Y
elif X == 5:
    res = 1.5 * Y

print(f'Total: R$ {res:0.2f}')