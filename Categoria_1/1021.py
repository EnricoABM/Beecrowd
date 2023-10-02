'''
Read a value of floating point with two decimal places. This represents
a monetary value. After this, calculate the smallest possible number of
notes and coins on which the value can be decomposed. The considered notes
 are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25,
 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of
 notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the
initial value, as the given example.

'''

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