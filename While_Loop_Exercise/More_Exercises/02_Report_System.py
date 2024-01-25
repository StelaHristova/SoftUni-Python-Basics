sum_sales = int(input())
price = input()

sum_subjects_cash = 0
sum_subjects_card = 0
sum_subjects = 0
count_subjects = 0
count_cash = 0
count_card = 0
is_enough = False

while price != 'End':
    price_subjects = int(price)
    count_subjects += 1
    if count_subjects % 2 != 0:
        if price_subjects > 100:
            print('Error in transaction!')
        else:
            sum_subjects_cash += price_subjects
            count_cash += 1
            print('Product sold!')
    else:
        if price_subjects < 10:
            print('Error in transaction!')
        else:
            sum_subjects_card += price_subjects
            count_card += 1
            print('Product sold!')

    sum_subjects = sum_subjects_cash + sum_subjects_card
    if sum_subjects >= sum_sales:
        is_enough = True
        break
    price = input()
if is_enough:
    print(f'Average CS: {sum_subjects_cash / count_cash:.2f}')
    print(f'Average CC: {sum_subjects_card / count_card:.2f}')
if price == 'End' and sum_subjects <= sum_sales:
     print('Failed to collect required money for charity.')
