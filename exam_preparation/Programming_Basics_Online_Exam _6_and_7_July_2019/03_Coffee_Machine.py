drink = input()
sugar = input()
count_drinks = int(input())

if drink == 'Espresso' and sugar == 'Without':
    price = 0.90
elif drink == 'Espresso' and sugar == 'Normal':
    price = 1
elif drink == 'Espresso' and sugar == 'Extra':
    price = 1.20
elif drink == 'Cappuccino' and sugar == 'Without':
    price = 1
elif drink == 'Cappuccino' and sugar == 'Normal':
    price = 1.20
elif drink == 'Cappuccino' and sugar == 'Extra':
    price = 1.60
elif drink == 'Tea' and sugar == 'Without':
    price = 0.50
elif drink == 'Tea' and sugar == 'Normal':
    price = 0.60
elif drink == 'Tea' and sugar == 'Extra':
    price = 0.70

total_price = count_drinks * price

if sugar == 'Without':
    total_price *= 0.65
if drink == 'Espresso' and count_drinks >= 5:
    total_price *= 0.75
if total_price > 15:
    total_price *= 0.80

print(f'You bought {count_drinks} cups of {drink} for {total_price:.2f} lv.')