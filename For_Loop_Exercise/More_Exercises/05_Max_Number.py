import sys

n = int(input())
max_num = -sys.maxsize

for i in range(n):
    num = int(input())
    if num > max_num:
        max_num = num
    print(f"{max_num}")