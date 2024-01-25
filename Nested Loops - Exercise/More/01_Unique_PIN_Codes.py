num1 = int(input())
num2 = int(input())
num3 = int(input())
is_prime = False
is_valid = False
for i in range(1, num1 + 1):
    for j in range(2, num2 + 1):
        for k in range(1, num3 + 1):
            count = 0
            is_valid = i % 2 == 0 and k % 2 == 0
            is_prime = j == 2 or j == 3 or j == 5 or j == 7

            if is_valid and is_prime:
                print(f'{i} {j} {k}')






