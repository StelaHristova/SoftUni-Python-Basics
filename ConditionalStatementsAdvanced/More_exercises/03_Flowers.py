count_chrysanthemums = int(input())
count_roses = int(input())
count_tulips = int(input())
season = input()
is_holiday = input()

price_chrysanthemums_spring_summer = 2.00
price_roses_spring_summer = 4.10
price_tulips_spring_summer = 2.50

price_chrysanthemums_autumn_winter = 3.75
price_roses_autumn_winter = 4.50
price_tulips_autumn_winter = 4.15

if season == "Spring":
    total_sum = count_chrysanthemums * price_chrysanthemums_spring_summer + count_roses * price_roses_spring_summer\
                + count_tulips * price_tulips_spring_summer
elif season == "Summer":
    total_sum = count_chrysanthemums * price_chrysanthemums_spring_summer + count_roses * price_roses_spring_summer\
                + count_tulips * price_tulips_spring_summer
elif season == "Autumn":
    total_sum = count_chrysanthemums * price_chrysanthemums_autumn_winter + count_roses * price_roses_autumn_winter\
                + count_tulips * price_tulips_autumn_winter
elif season == "Winter":
    total_sum = count_chrysanthemums * price_chrysanthemums_autumn_winter + count_roses * price_roses_autumn_winter \
                + count_tulips * price_tulips_autumn_winter

holiday_tax = 0

if is_holiday == "Y":
    holiday_tax += 0.15 * total_sum

total_sum = total_sum + holiday_tax

if count_tulips > 7 and season == "Spring":
    total_sum -= 0.05 * total_sum
if count_roses >= 10 and season == "Winter":
    total_sum -= 0.10 * total_sum
if (count_chrysanthemums + count_roses + count_tulips) > 20:
    total_sum -= 0.20 * total_sum


print(f"{total_sum + 2:.2f}")