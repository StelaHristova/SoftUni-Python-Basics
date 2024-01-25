type = input()
liters = float(input())

if liters >= 25:
    if type == "Diesel" or type =="Gasoline" or type == "Gas":
        result = type[0].lower() + type[1:]
        print(f"You have enough {result}.")
    else:
        print(f"Invalid fuel!")
if liters < 25:
    if type == "Diesel" or type =="Gasoline" or type == "Gas":
        result = type[0].lower() + type[1:]
        print(f"Fill your tank with {result}!")
    else:
        print(f"Invalid fuel!")
