def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

floor_first_num = int(input())
floor_second_num = int(input())
diff_first_num = int(input())
diff_second_num = int(input())

a = floor_first_num + diff_first_num
b = floor_second_num + diff_second_num

for first in range(floor_first_num, a + 1):
    for second in range(floor_second_num, b + 1):
        if is_prime(first) and is_prime(second):
            print(f'{first}{second}')





'''n = int(input())
is_prime = True

for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0:
        is_prime = False
        break
if is_prime:
    print('Prime')
else:
    print('Not prime')

if n < 2 or n < 0:
    print('Not prime')'''