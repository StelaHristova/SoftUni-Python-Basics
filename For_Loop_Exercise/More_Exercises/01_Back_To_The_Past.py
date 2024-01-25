inherited_money = float(input())
total_money = 0
diff = 0
years_old = 0
year_to_live = int(input())
diff = inherited_money - total_money

for i in range(1800, year_to_live + 1):
    if i % 2 == 0:
        total_money = 12000
        diff = diff - total_money
    else:
        years_old = 18 + (i - 1800)
        total_money = total_money + years_old * 50
        diff = diff - total_money

if diff >= 0:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {abs(diff):.2f} dollars to survive.")