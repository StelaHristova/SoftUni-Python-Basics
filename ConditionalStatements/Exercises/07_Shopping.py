budget = float(input())
count_videocard = int(input())
count_cpu = int(input())
count_ram = int(input())

sum_videocard = count_videocard * 250
sum_cpu = count_cpu * (0.35 * sum_videocard)
sum_ram = count_ram * (0.1 * sum_videocard)
total_sum = sum_videocard + sum_cpu + sum_ram

if count_videocard > count_cpu:
    total_sum *= 85 / 100

if total_sum <= budget:
    print(f"You have {budget-total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")