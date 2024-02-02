T = int(input())

A, B, C, D, E = map(int, input().split())

lista = [A, B, C, D, E]

count = 0
for item in lista:
    if item == T:
        count += 1
print(count)
