capacity_stadium = int(input())
count_fans = int(input())
fans_A, fans_B, fans_V, fans_G = 0, 0, 0, 0

for i in range(count_fans):
    sector = input()
    if sector == "A":
        fans_A += 1
    elif sector == 'B':
        fans_B += 1
    elif sector == 'V':
        fans_V += 1
    elif sector == 'G':
        fans_G += 1

print(f'{fans_A * 100 / count_fans:.2f}%')
print(f'{fans_B * 100 / count_fans:.2f}%')
print(f'{fans_V * 100 / count_fans:.2f}%')
print(f'{fans_G * 100 / count_fans:.2f}%')
print(f'{count_fans * 100 / capacity_stadium:.2f}%')