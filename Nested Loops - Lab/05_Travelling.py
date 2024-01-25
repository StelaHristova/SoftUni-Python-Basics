while True:
    destination = input()

    if destination == 'End':
        break

    excursion_price = float(input())
    current_money = 0

    while current_money < excursion_price:
        current_money += float(input())

    print(f'Going to {destination}!')