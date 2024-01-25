age = int(input())
price_of_washing_mashine = float(input())
present_price = int(input())

number_of_toys = 0
saved_money = 0
money_for_birthday = 10

for current_year in range(1, age + 1):
    if current_year % 2 == 0:
        saved_money += (money_for_birthday - 1)
        money_for_birthday += 10
    else:
        number_of_toys += 1

saved_money += number_of_toys * present_price

diff = abs(saved_money - price_of_washing_mashine)

if saved_money >= price_of_washing_mashine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")