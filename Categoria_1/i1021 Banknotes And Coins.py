'''
INCOMPLETO
lista = [100, 50, 20, 10, 5, 2, 1]
lista2 =  [0.5, 0.25, 0.1, 0.05, 0.01]

N = float(input())
resto = N
nm = []

for num in lista:
    nm.append(resto//num)
    resto = resto % num

for num in lista2:
    nm.append(resto/num)
    resto = resto % num
print(nm)
print("NOTAS: ")
print(f"{nm[0]} nota(s) de R$ 100.00")
print(f"{nm[1]} nota(s) de R$ 50.00")
print(f"{nm[2]} nota(s) de R$ 20.00")
print(f"{nm[3]} nota(s) de R$ 10.00")
print(f"{nm[4]} nota(s) de R$ 5.00")
print(f"{nm[5]} nota(s) de R$ 2.00")
print("MOEDAS: ")
print(f"{nm[6]:.0f} moeda(s) de R$ 1.00")
print(f"{nm[7]:.0f} moeda(s) de R$ 0.50")
print(f"{nm[8]:.0f} moeda(s) de R$ 0.25")
print(f"{nm[9]:.0f} moeda(s) de R$ 0.10")
print(f"{nm[10]:.0f} moeda(s) de R$ 0.05")
print(f"{nm[11]:.0f} moeda(s) de R$ 0.01")
'''