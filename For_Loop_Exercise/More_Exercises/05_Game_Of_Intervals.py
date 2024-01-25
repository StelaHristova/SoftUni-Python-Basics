n = int(input())
points1, points2, points3, points4, points5, points6 = 0, 0, 0, 0, 0, 0
count1, count2, count3, count4, count5, count6 = 0, 0, 0, 0, 0, 0
for i in range(n):
    moves = int(input())
    if 0 <= moves <= 9:
        points1 += 0.2 * moves
        count1 += 1
    elif 10 <= moves <= 19:
        points2 += 0.3 * moves
        count2 += 1
    elif 20 <= moves <= 29:
        points3 += 0.4 * moves
        count3 += 1
    elif 30 <= moves <= 39:
        points4 += 50
        count4 += 1
    elif 40 <= moves <= 50:
        points5 += 100
        count5 += 1
    else:
        points6 -= (points1 + points2 + points3 + points4 + points5 + points6) / 2
        count6 += 1
        
print(f'{(points1 + points2 + points3 + points4 + points5 + points6):.2f}')
print(f'From 0 to 9: {count1 * 100 / n:.2f}%')
print(f'From 10 to 19: {count2 * 100 / n:.2f}%')
print(f'From 20 to 29: {count3 * 100 / n:.2f}%')
print(f'From 30 to 39: {count4 * 100 / n:.2f}%')
print(f'From 40 to 50: {count5 * 100 / n:.2f}%')
print(f'Invalid numbers: {count6 * 100 / n:.2f}%')