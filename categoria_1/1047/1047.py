class Jogo:
    def __init__(self, horas_inicio, minutos_inicio, horas_fim, minutos_fim):
        self.horas_inicio = horas_inicio
        self.horas_fim = horas_fim
        self.minutos_inicio = minutos_inicio
        self.minutos_fim = minutos_fim

    def calcular(self):
        total_minutos_inicio = self.horas_inicio * 60 + self.minutos_inicio
        total_minutos_fim = self.horas_fim * 60 + self.minutos_fim
        if total_minutos_inicio < total_minutos_fim:
            horas = (total_minutos_fim - total_minutos_inicio) // 60
            minutos = (total_minutos_fim - total_minutos_inicio) % 60
        elif total_minutos_inicio == total_minutos_fim:
            horas = 24
            minutos = 0
        else:
            total_minutos_fim += 24 * 60
            horas = (total_minutos_fim - total_minutos_inicio) // 60
            minutos = (total_minutos_fim - total_minutos_inicio) % 60
        return [horas, minutos]


a, b, c, d = map(int, input().split())
j1 = Jogo(a, b, c, d)
horas_minutos = j1.calcular()
msg = f'O JOGO DUROU {horas_minutos[0]} HORA(S) E {horas_minutos[1]} MINUTO(S)'
print(msg)
