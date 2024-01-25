weight_package = float(input())
type_favor = input()
distance = int(input())

if type_favor == 'standard':
    if weight_package < 1:
        price = 0.03
    elif 1 <= weight_package < 10:
        price = 0.05
    elif 10 <= weight_package < 40:
        price = 0.10
    elif 40 <= weight_package < 90:
        price = 0.15
    elif 90 <= weight_package < 150:
        price = 0.20
elif type_favor == 'express':
    if weight_package < 1:
        price = 0.03 + weight_package * 0.8 * 0.03
    elif 1 <= weight_package < 10:
        price = 0.05 + weight_package * 0.4 * 0.05
    elif 10 <= weight_package < 40:
        price = 0.10 + weight_package * 0.05 * 0.10
    elif 40 <= weight_package < 90:
        price = 0.15 + weight_package * 0.02 * 0.15
    elif 90 <= weight_package < 150:
        price = 0.20 + weight_package * 0.01 * 0.20

print(f'The delivery of your shipment with weight of {weight_package:.3f} kg. would cost {price * distance:.2f} lv.')