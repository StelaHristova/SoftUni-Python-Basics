price_trip = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_tinder = int(input())
count_minions = int(input())
count_trucks = int(input())

price_puzzle = 2.60
price_dolls = 3
price_tinder = 4.10
price_minions = 8.20
price_trucks = 2

total_sum = count_puzzles * price_puzzle + count_dolls * price_dolls + count_tinder * price_tinder +\
            count_minions * price_minions + count_trucks * price_trucks
count_toys = count_puzzles + count_dolls + count_tinder + count_minions + count_trucks

if count_toys >= 50:
    total_sum *= 75 / 100

total_sum *= 90 / 100

if total_sum >= price_trip:
    print(f"Yes! {total_sum-price_trip:.2f} lv left.")
else:
    print(f"Not enough money! {price_trip - total_sum:.2f} lv needed.")