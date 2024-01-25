import sys

n = int(input())
min_num = sys.maxsize

for i in range(n):
    num = int(input())
    if num < min_num:
        min_num = num
        print(f'{min_num}')