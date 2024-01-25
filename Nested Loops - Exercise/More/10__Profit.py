count_coins_1_lv = int(input())
count_coins_2_lv = int(input())
count_coins_5_lv = int(input())
sum_money = int(input())

for i in range(0, count_coins_1_lv + 1):
    for j in range(0, count_coins_2_lv + 1):
        for k in range(0, count_coins_5_lv + 1):
            if i * 1 + j * 2 + k * 5 == sum_money:
                print(f'{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {sum_money} lv.')
