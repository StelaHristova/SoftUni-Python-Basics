profit_wanted = float(input())
profit = 0
while profit < profit_wanted:
    drink_name = input()

    if drink_name == "Party":
        print(f'We need {profit_wanted - profit:.2f} leva more.')
        break

    drink_price = int(input())

    bill = len(drink_name) * drink_price

    if bill % 2 == 1:
        bill *= 0.75

    profit += bill

else:
    print(f'Target acquired.')

print(f'Club income - {profit:.2f} leva.')