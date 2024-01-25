hours = int(input())
minutes = int(input())
minutes_new = (minutes + 15) % 60
hours_new = hours + (minutes + 15) // 60

if minutes_new < 10:
    print(f"{hours_new}:0{minutes_new}")
elif hours_new > 23:
    print(f"{24 - hours_new}:{minutes_new}")
else:
    print(f"{hours_new}:{minutes_new}")

