count_pen = int(input())
count_markers = int(input())
detergent_liters = int(input())
discount = int(input())

total_sum = (count_pen * 5.80) + (count_markers * 7.20) + (detergent_liters * 1.20)
total_sum -= (total_sum * discount / 100)

print(total_sum)