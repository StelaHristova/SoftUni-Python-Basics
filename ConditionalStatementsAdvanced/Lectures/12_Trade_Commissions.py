city = input()
sales = float(input())
comission = 'error'
if city == "Sofia":
    if 0 <= sales <= 500:
        comission = sales * 5 / 100
    elif 500 < sales <= 1000:
        comission = sales * 7 / 100
    elif 1000 < sales <= 10000:
        comission = sales * 8 / 100
    elif sales > 10000:
        comission = sales * 12 / 100
elif city == "Varna":
    if 0 <= sales <= 500:
        comission = sales * 4.5 / 100
    elif 500 < sales <= 1000:
        comission = sales * 7.5 / 100
    elif 1000 < sales <= 10000:
        comission = sales * 10 / 100
    elif sales > 10000:
        comission = sales * 13 / 100
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        comission = sales * 5.5 / 100
    elif 500 < sales <= 1000:
        comission = sales * 8 / 100
    elif 1000 < sales <= 10000:
        comission = sales * 12 / 100
    elif sales > 10000:
        comission = sales * 14.5 / 100

if comission == "error":
    print(comission)
else:
    print(f"{comission:.2f}")