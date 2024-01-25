budget = float(input())
count_nights = int(input())
price_for_night = float(input())
percentage_for_other_costs = int(input())

if count_nights > 7:
    price_for_night *= 0.95

price_all_nights = count_nights * price_for_night
other_costs = percentage_for_other_costs * budget / 100
total_costs = price_all_nights + other_costs

if total_costs <= budget:
    print(f'Ivanovi will be left with {budget - total_costs:.2f} leva after vacation.')
else:
    print(f'{total_costs - budget:.2f} leva needed.')