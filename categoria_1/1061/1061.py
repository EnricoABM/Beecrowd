first_input = input().split()
first_day = int(first_input[1])

first_time = input().split(":")
first_hour = int(first_time[0])
first_minutes = int(first_time[1])
first_seconds = int(first_time[2])

first_total_seconds = first_day * 86400 + \
                    first_hour * 3600 + \
                    first_minutes * 60 + \
                    first_seconds

final_input = input().split()
final_day = int(final_input[1])

final_time = input().split(':')
final_hour = int(final_time[0])
final_minutes = int(final_time[1])
final_seconds = int(final_time[2])

final_total_seconds = final_day * 86400 + \
                    final_hour * 3600 + \
                    final_minutes * 60 + \
                    final_seconds

total_seconds = final_total_seconds - first_total_seconds

W = total_seconds // 86400
total_seconds %= 86400
X = total_seconds // 3600
total_seconds %= 3600
Y = total_seconds // 60
total_seconds %= 60
Z = total_seconds

print(f"{W} dia(s)")
print(f"{X} hora(s)")
print(f"{Y} minuto(s)")
print(f"{Z} segundo(s)")
