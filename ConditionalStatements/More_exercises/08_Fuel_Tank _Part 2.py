type_fuel = input()
qty_fuel = float(input())
club_card = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93
total_sum = 0

if club_card == "Yes":
    if type_fuel == "Gasoline":
        gasoline -= 0.18
        total_sum = gasoline * qty_fuel
    elif type_fuel == "Diesel":
        diesel -= 0.12
        total_sum = diesel * qty_fuel
    elif type_fuel == "Gas":
        gas -= 0.08
        total_sum = gas * qty_fuel
else:
    if type_fuel == "Gasoline":
        total_sum = gasoline * qty_fuel
    elif type_fuel == "Diesel":
       total_sum = diesel * qty_fuel
    elif type_fuel == "Gas":
        total_sum = gas * qty_fuel

if type_fuel == "Gasoline" or type_fuel == "Diesel" or type_fuel =="Gas":
    if 20 <= qty_fuel <= 25:
        total_sum *= 0.92
    elif qty_fuel > 25:
        total_sum *= 0.90

print(f"{total_sum:.2f} lv.")