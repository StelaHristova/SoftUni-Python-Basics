season = input()
km_per_month = float(input())

if km_per_month <= 5000:
    if season == "Spring":
        salary = km_per_month * 0.75 * 4
    if season == "Summer":
        salary = km_per_month * 0.90 * 4
    if season == "Autumn":
        salary = km_per_month * 0.75 * 4
    if season == "Winter":
        salary = km_per_month * 1.05 * 4
elif 5000 < km_per_month <= 10000:
    if season == "Spring":
        salary = km_per_month * 0.95 * 4
    if season == "Summer":
        salary = km_per_month * 1.10 * 4
    if season == "Autumn":
        salary = km_per_month * 0.95 * 4
    if season == "Winter":
        salary = km_per_month * 1.25 * 4
else:
     salary = km_per_month * 1.45 * 4

salary = salary - 0.10 * salary
print(f"{salary:.2f}")