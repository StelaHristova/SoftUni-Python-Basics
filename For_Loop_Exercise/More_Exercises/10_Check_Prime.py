import math
n = int(input())
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
    print('Not prime')