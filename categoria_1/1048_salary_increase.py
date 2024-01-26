"""
0 - 400.00          15%
400.01 - 800.00     12%
800.01 - 1200.00    10%
1200.01 - 2000.00   7%
Above 2000.00       4%
"""

def between_in(valor, v1, v2):
    if valor >= v1 and valor <= v2:
        return True
    return False

class SalaryIncrease:
    def __init__(self, salario):
        self.salario = salario
    
    def aumento(self):
        if between_in(self.salario, 0, 400):
            percent = 15
        elif between_in(self.salario, 401, 800):
            percent = 12
        elif between_in(self.salario, 800.01, 1200):
            percent = 10
        elif between_in(self.salario, 1200.01, 2000):
            percent = 7
        else: 
            percent = 4

        percent_in_money = self.salario * (percent/100)
        new_salary = self.salario + percent_in_money
        return {"novo salario": new_salary, "percentual": percent, "acrescimo": percent_in_money}
    
N = float(input())

salario = SalaryIncrease(N)
novo_salario = salario.aumento()

print(f'Novo salario: {novo_salario["novo salario"]:.2f}')
print(f'Reajuste ganho: {novo_salario["acrescimo"]:.2f}')
print(f'Em percentual: {novo_salario["percentual"]} %') 
