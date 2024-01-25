k = int(input())
l = int(input())
m = int(input())
n = int(input())
is_possible = False
is_valid = False
valid = 0

for i in range(k, 9):
    for j in range(9, l - 1, -1):
        for p in range(m, 9):
            for q in range(9, n - 1, -1):
                if k % 2 != 0 and m % 2 == 0:
                    if i % 2 != 0 and p % 2 == 0 and j % 2 != 0 and q % 2 != 0:
                        is_possible = True
                        if (i != p and j == q) or (i == p and j != q):
                            is_valid = True
                            valid += 1
                        if valid == 6:
                            break
                    if is_possible and is_valid:
                        print(f'{i}{j} - {p}{q}')
                    elif is_possible == True and is_valid == False:
                        print(f'Cannot change the same player.')
                elif k % 2 == 0 and m % 2 == 0:
                    if i % 2 != 0 and p % 2 != 0 and j % 2 != 0 and q % 2 != 0:
                        is_possible = True
                        if (i != p and j == q) or (i == p and j != q):
                            is_valid = True
                            valid += 1
                        if valid == 6:
                            break
                    if is_possible and is_valid:
                        print(f'{i}{j} - {p}{q}')
                    elif is_possible == True and is_valid == False:
                        print(f'Cannot change the same player.')

                elif k % 2 == 0 and m % 2 != 0:
                    if i % 2 != 0 and p % 2 == 0 and j % 2 != 0 and q % 2 != 0:
                        is_possible = True
                        if (i != p and j == q) or (i == p and j != q):
                            is_valid = True
                            valid += 1
                        if valid == 6:
                            break
                    if is_possible and is_valid:
                        print(f'{i}{j} - {p}{q}')
                    elif is_possible == True and is_valid == False:
                        print(f'Cannot change the same player.')
                elif k % 2 != 0 and m % 2 != 0:
                    if i % 2 == 0 and p % 2 == 0 and j % 2 != 0 and q % 2 != 0:
                        is_possible = True
                        if (i != p and j == q) or (i == p and j != q):
                            is_valid = True
                            valid += 1
                        if valid == 6:
                            break
                    if is_possible and is_valid:
                        print(f'{i}{j} - {p}{q}')
                    elif is_possible == True and is_valid == False:
                        print(f'Cannot change the same player.')