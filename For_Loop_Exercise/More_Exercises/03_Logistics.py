n= int(input())
price_van, price_truck, price_train = 0, 0, 0
load_van, load_truck, load_train = 0, 0, 0
total_load = 0
percentage_van, percentage_truck, percentage_train = 0, 0, 0
average = 0
for i in range(n):
    ton_load = int(input())
    total_load += ton_load
    if ton_load <= 3:
        price_van += 200 * ton_load
        load_van += ton_load
    elif 4 <= ton_load <= 11:
        price_truck += 175 * ton_load
        load_truck += ton_load
    elif ton_load >= 12:
        price_train += 120 * ton_load
        load_train += ton_load

average = (price_van + price_truck + price_train) / total_load
percentage_van = load_van * 100 / total_load
percentage_truck = load_truck * 100 / total_load
percentage_train = load_train * 100 / total_load

print(f"{average:.2f}")
print(f"{percentage_van:.2f}%")
print(f"{percentage_truck:.2f}%")
print(f"{percentage_train:.2f}%")