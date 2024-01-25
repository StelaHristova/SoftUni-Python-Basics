import math

count_days = int(input())
left_food = int(input())
food_dog_per_day_kg = float(input())
food_cat_per_day_kg = float(input())
food_turtle_per_day_g = float(input())

food_dog = count_days * food_dog_per_day_kg
food_cat = count_days * food_cat_per_day_kg
food_turtle = count_days * food_turtle_per_day_g / 1000

total_food = food_dog + food_cat + food_turtle

if total_food <= left_food:
    diff = math.floor(abs(left_food - total_food))
    print(f"{diff} kilos of food left.")
else:
    diff = math.ceil(abs(left_food - total_food))
    print(f"{diff} more kilos of food are needed.")