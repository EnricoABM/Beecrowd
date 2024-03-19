posCount = 0
negCount = 0
parCount = 0
imparCount = 0

for i in range(5):
    valor = int(input())
    if valor % 2 == 0:
        parCount += 1
    else:
        imparCount += 1
    
    if valor > 0:
        posCount += 1
    elif valor < 0:
        negCount += 1

print(f"{parCount} valor(es) par(es)")
print(f"{imparCount} valor(es) impar(es)")
print(f"{posCount} valor(es) positivo(s)")
print(f"{negCount} valor(es) negativo(s)")
