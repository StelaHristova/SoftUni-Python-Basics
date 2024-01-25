import math

count_magnoliaa = int(input())
count_hyacinthes = int(input())
count_roses = int(input())
count_cactuses = int(input())
gift_price = float(input())

total_sum = count_magnoliaa * 3.25 + count_hyacinthes * 4 + count_roses * 3.50 + count_cactuses * 8
total_sum *= 0.95

if total_sum < gift_price:
    diff = math.ceil(abs(total_sum - gift_price))
    print(f"She will have to borrow {diff} leva.")

else:
    diff = math.floor(abs(total_sum - gift_price))
    print(f"She is left with {diff} leva.")