hours = int(input())
minutes = int(input())
minutes_new = (minutes + 15) % 60
hours_new = hours + (minutes + 15) // 60

if hours_new > 23:
    hours_new = 0
if minutes_new < 10:
    print(f"{hours_new}:0{minutes_new}")
else:
    print(f"{hours_new}:{minutes_new}")

