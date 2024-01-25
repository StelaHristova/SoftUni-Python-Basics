VIP = 499.99
Normal = 249.99

budget = float(input())
category = input()
count_people_in_group = int(input())

if 1 <= count_people_in_group <= 4:
    transport = 0.75 * budget
elif 5 <= count_people_in_group <= 9:
    transport = 0.60 * budget
elif 10 <= count_people_in_group <= 24:
    transport = 0.50 * budget
elif 25 <= count_people_in_group <= 49:
    transport = 0.40 * budget
else:
    transport = 0.25 * budget

total_sum = budget - transport

if category =="VIP":
    price_ticket = VIP * count_people_in_group
else:
    price_ticket = Normal * count_people_in_group

if price_ticket < total_sum:
    print(f"Yes! You have {total_sum - price_ticket:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(total_sum - price_ticket):.2f} leva.")