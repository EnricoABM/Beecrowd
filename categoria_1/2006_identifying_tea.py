T = int(input())
A, B, C, D, E = map(int,input().split())
l = [A,B,C,D,E]
count = 0
for item in l:
    if item == T:
        count += 1
print(count)

