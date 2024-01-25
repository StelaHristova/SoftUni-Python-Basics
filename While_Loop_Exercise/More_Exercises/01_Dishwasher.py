detergent = int(input())
count_detergent = detergent * 750
count_dishes = input()
loaded_dishes = 0
loaded_pots = 0
remainder_dishes = count_detergent - loaded_dishes
pure_dishes = 0
pure_pots = 0
is_enough = False
dish_counter = 0

while remainder_dishes >= 0:
    if count_dishes == 'End':
        is_enough = True
        break
    dishes = int(count_dishes)
    dish_counter += 1
    if dish_counter % 3 != 0:
        loaded_dishes = dishes * 5
        remainder_dishes -= loaded_dishes
        pure_dishes += dishes
    else:
        loaded_pots = dishes * 15
        remainder_dishes -= loaded_pots
        pure_pots += dishes
    if remainder_dishes < 0:
        break
    count_dishes = input()

if is_enough:
    print(f'Detergent was enough!')
    print(f'{pure_dishes} dishes and {pure_pots} pots were washed.')
    print(f'Leftover detergent {remainder_dishes} ml.')
else:
    print(f'Not enough detergent, {abs(remainder_dishes)} ml. more necessary!')


