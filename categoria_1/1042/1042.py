# Com sort()
a, b, c = map(int, input().split())
lista = [a, b, c]
lista.sort()
for item in lista:
    print(item)
print()
print(a, b, c, sep='\n')
