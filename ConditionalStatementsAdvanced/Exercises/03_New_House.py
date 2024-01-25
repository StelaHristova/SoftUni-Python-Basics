type_flowers = input()
count_flowers = int(input())
budget = int(input())

sum = 0

if type_flowers == "Roses":
    if count_flowers <= 80:
        sum = count_flowers * 5
    elif count_flowers > 80:
        sum = count_flowers * 5 * 0.9
elif type_flowers == "Dahlias":
    if count_flowers <= 90:
        sum = count_flowers * 3.80
    elif count_flowers > 90:
        sum = count_flowers * 3.80 * 0.85
elif type_flowers == "Tulips":
    if count_flowers <= 80:
        sum = count_flowers * 2.80
    elif count_flowers > 80:
        sum = count_flowers * 2.80 * 0.85
elif type_flowers == "Narcissus":
        if count_flowers < 120:
            sum = count_flowers * 3 * 1.15
        elif count_flowers >= 120:
            sum = count_flowers * 3
elif type_flowers == "Gladiolus":
        if count_flowers < 80:
            sum = count_flowers * 2.50 * 1.20
        elif count_flowers >= 80:
            sum = count_flowers * 2.50

total_sum = abs((budget - sum))

if budget >= sum:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {total_sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_sum:.2f} leva more.")