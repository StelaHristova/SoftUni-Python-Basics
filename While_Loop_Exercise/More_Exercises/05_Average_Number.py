n = int(input())
num = int(input())
count = 0
sum_n = 0
is_ready = False
while count < n:
    count += 1
    sum_n += num

    if count == n:
        is_ready = True
        break
    num = int(input())
if is_ready:
    print(f'{sum_n / count:.2f}')
