budget = int(input())
season = input()
count_fishers = int(input())
price_ship = 0

if season == "Spring":
    price_ship = 3000
elif season == "Summer" or season == "Autumn":
    price_ship = 4200
elif season == "Winter":
    price_ship = 2600

if count_fishers <= 6:
        price_ship *= 0.90
elif 7 <= count_fishers <= 11:
        price_ship *= 0.85
elif count_fishers >= 12:
        price_ship *= 0.75

if count_fishers % 2 == 0:
    if season != "Autumn":
        price_ship *= 0.95

money = abs((budget - price_ship))

if budget >= price_ship:
    print(f"Yes! You have {money:.2f} leva left.")
else:
    print(f"Not enough money! You need {money:.2f} leva.")