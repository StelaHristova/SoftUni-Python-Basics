month = input()
count_nights = int(input())

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77

price_for_apartment = count_nights * price_apartment
price_for_studio = count_nights * price_studio

if (7 < count_nights < 14 and month == "May") or (7 < count_nights < 14 and month == "October"):
    price_for_studio *= 0.95
elif (count_nights > 14 and month == "May") or (count_nights > 14 and month == "October"):
    price_for_studio *= 0.70
elif (count_nights > 14 and month == "June") or (count_nights > 14 and month == "September"):
    price_for_studio *= 0.80
if count_nights > 14:
    price_for_apartment *= 0.90

print(f"Apartment: {price_for_apartment:.2f} lv.")
print(f"Studio: {price_for_studio:.2f} lv.")