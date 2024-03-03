days_ = int(input())

years = days_ / 365
mouths = (days_ % 365) / 30
days = (days_ % 365) % 30

print(int(years), 'ano(s)')
print(int(mouths), "mes(es)")
print(days, "dia(s)")
