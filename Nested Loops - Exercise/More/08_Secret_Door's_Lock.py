ceil_hundreds = int(input())
ceil_dozens = int(input())
ceil_units = int(input())
is_valid = False
for i in range(1, ceil_hundreds + 1):
    for j in range(2, ceil_dozens + 1):
        is_valid = j == 2 or j == 3 or j == 5 or j == 7
        for k in range(1, ceil_units + 1):
            if i % 2 == 0 and k % 2 == 0 and is_valid:
                print(f'{i} {j} {k}')