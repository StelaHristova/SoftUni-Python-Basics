import math
from math import ceil
walls = 4
wall_height = int(input())
wall_width = int(input())
percentage_unpainted_walls = int(input())

area_to_paint = math.ceil(walls * wall_height * wall_width * (1 - percentage_unpainted_walls / 100))

while True:
    liters = input()

    if liters == 'Tired!':
       break

    liters = int(liters)

    area_to_paint -= liters

    if area_to_paint <= 0:
        break

if area_to_paint < 0:
    print(f'All walls are painted and you have {abs(area_to_paint)} l paint left!')
elif area_to_paint == 0:
    print(f'All walls are painted! Great job, Pesho!')
else:
    print(f'{area_to_paint} quadratic m left.')