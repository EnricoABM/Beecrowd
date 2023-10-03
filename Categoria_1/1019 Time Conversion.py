N = int(input())
hours = N // 3600
rest = N % 3600
minutes = rest // 60
rest = rest % 60 #TODO: Trocar a função
seconds = rest
print("{}:{}:{}".format(hours, minutes, seconds))
