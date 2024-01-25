city_name = input()
packet_name = input()
VIP_discount = input()
count_days = int(input())
is_valid = False

if (city_name == 'Bansko' and packet_name == 'withEquipment') or (city_name == 'Borovets' and packet_name == 'withEquipment'):
    price = 100
    is_valid = True
    if VIP_discount == 'yes':
        price *= 0.9
elif (city_name == 'Bansko' and packet_name == 'noEquipment') or (city_name == 'Borovets' and packet_name == 'noEquipment'):
    price = 80
    is_valid = True
    if VIP_discount == 'yes':
        price *= 0.95
elif (city_name == 'Varna' and packet_name == 'withBreakfast') or (city_name == 'Burgas' and packet_name == 'withBreakfast'):
    price = 130
    is_valid = True
    if VIP_discount == 'yes':
        price *= 0.88
elif (city_name == 'Varna' and packet_name == 'noBreakfast') or (city_name == 'Burgas' and packet_name == 'noBreakfast'):
    price = 100
    is_valid = True
    if VIP_discount == 'yes':
        price *= 0.93

if count_days > 7:
    count_days -= 1

if count_days < 1:
    print(f'Days must be positive number!')
elif is_valid:
    print(f'The price is {price * count_days:.2f}lv! Have a nice time!')
else:
    print(f'Invalid input!')