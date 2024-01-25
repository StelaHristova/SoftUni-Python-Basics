days = int(input())
type_room = input()
rating = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35

nights = days - 1
total_price = 0

if type_room == "room for one person":
    total_price = (nights * room_for_one_person)
elif type_room == "apartment":
    if nights < 10:
        total_price = (nights * apartment) * 0.70
    elif 10 < nights < 15:
        total_price = (nights * apartment) * 0.65
    elif nights > 15:
        total_price = (nights * apartment) * 0.50
elif type_room == "president apartment":
    if nights < 10:
        total_price = (nights * president_apartment) * 0.90
    elif 10 < nights < 15:
        total_price = (nights * president_apartment) * 0.85
    elif nights > 15:
        total_price = (nights * president_apartment) * 0.80

if rating == "positive":
    total_price *= 1.25
elif rating == "negative":
    total_price *= 0.90

print(f"{total_price:.2f}")