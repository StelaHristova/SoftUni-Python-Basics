number = float(input())
source_metric = input().lower()
dest_metric = input().lower()

if source_metric == "m":
    number = number
elif source_metric == "mm":
    number = number / 1000
elif source_metric == "cm":
    number = number / 100
elif source_metric == "mi":
    number = number / 0.000621371192
elif source_metric == "in":
    number = number / 39.3700787
elif source_metric == "km":
    number = number * 1000
elif source_metric == "ft":
    number = number / 3.2808399
elif source_metric == "yd":
    number = number / 1.0936133

if dest_metric == "m":
    number = number
elif dest_metric == "mm":
    number = number * 1000
elif dest_metric == "cm":
    number = number * 100
elif dest_metric == "mi":
    number = number * 0.000621371192
elif dest_metric == "in":
    number = number * 39.3700787
elif dest_metric == "km":
    number = number / 1000
elif dest_metric == "ft":
    number = number * 3.2808399
elif dest_metric == "yd":
    number = number * 1.0936133

print(f"{number} {dest_metric}")