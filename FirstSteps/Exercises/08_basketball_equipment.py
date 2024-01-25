year_tax = int(input())

price_basketball_snickers = year_tax - year_tax * 40 / 100
price_basketball_clothes = price_basketball_snickers - price_basketball_snickers * 20 / 100
price_basketball_ball = (1 / 4) * price_basketball_clothes
price_basketball_accessories = (1/5) * price_basketball_ball
total_price = year_tax + price_basketball_snickers + price_basketball_clothes + price_basketball_ball + price_basketball_accessories

print(total_price)