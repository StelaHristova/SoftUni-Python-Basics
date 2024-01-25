import sys

count_numbers = int(input())
sum_numbers = 0
max_number = -sys.maxsize

for i in range(0, count_numbers):
    num = int(input())
    if num > max_number:
        max_number = num
    sum_numbers += num

sum_numbers = sum_numbers - max_number
if max_number == sum_numbers:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    diff = abs(max_number - sum_numbers)
    print(f"Diff = {diff}")
