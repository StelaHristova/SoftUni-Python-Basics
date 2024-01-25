M = int(input())
counter = 0
is_valid = False
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a * b + c * d == M) and a < b and c > d:
                    counter += 1
                    print(f'{a}{b}{c}{d}', end=' ')

                    if counter == 4:
                        a4 = a
                        b4 = b
                        c4 = c
                        d4 = d
                is_valid = (a * b + c * d == M) and a < b and c > d
if counter >= 4 or is_valid:
    print()
    print(f'Password: {a4}{b4}{c4}{d4}')
else:
    print()
    print(f'No!')

