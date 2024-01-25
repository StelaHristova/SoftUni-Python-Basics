profit_wanted = float(input())
profit = 0

while profit_wanted > profit:
    cocktail_name = input()

    if cocktail_name == 'Party!':
        print(f'We need {profit_wanted - profit:.2f} leva more.')
        break

    count_cocktails = int(input())

    price_cocktails = len(cocktail_name) * count_cocktails

    if price_cocktails % 2 == 1:
        price_cocktails *= 0.75
    profit += price_cocktails

else:
    print(f'Target acquired.')

print(f'Club income - {profit:.2f} leva.')



