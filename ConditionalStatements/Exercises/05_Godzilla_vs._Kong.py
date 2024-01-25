budget = float(input())
count_actors = int(input())
price_outfit_per_actor = float(input())

decor = budget * 10 / 100

if count_actors >= 150:
    price_outfit_per_actor *= 90 / 100

total_sum_outfit = count_actors * price_outfit_per_actor
total_sum = total_sum_outfit + decor
left_money = abs(total_sum-budget)

if total_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {left_money:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")