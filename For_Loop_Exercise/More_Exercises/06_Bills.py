months = int(input())
power = 0
other = 0
average = 0
for i in range(months):
    electricity = float(input())
    water = months * 20
    internet = months * 15
    power += electricity
    other += (electricity + 20 + 15) * 1.2
    average += (electricity + 20 + 15 + (electricity + 20 + 15) * 1.2) / months

print(f'Electricity: {power:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')