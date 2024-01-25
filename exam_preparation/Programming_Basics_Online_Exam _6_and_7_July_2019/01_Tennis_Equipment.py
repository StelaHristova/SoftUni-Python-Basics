import math

price_for_one_tennis_rocket = float(input())
count_tennis_rockets = int(input())
count_pairs_snickers = int(input())

price_all_rockets = count_tennis_rockets * price_for_one_tennis_rocket
price_for_pair_snickers = price_for_one_tennis_rocket / 6
price_all_pairs_snickers = count_pairs_snickers * price_for_pair_snickers
price_others = (price_all_rockets + price_all_pairs_snickers) * 0.20
total_price = price_all_rockets + price_all_pairs_snickers + price_others
price_djokovic = math.floor(total_price / 8)
price_sponsors = math.ceil(total_price * 7 / 8)

print(f'Price to be paid by Djokovic {price_djokovic}')
print(f'Price to be paid by sponsors {price_sponsors}')