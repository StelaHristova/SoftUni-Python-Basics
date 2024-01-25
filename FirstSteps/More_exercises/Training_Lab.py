w = float(input())
h = float(input())

places_width = (h * 100 - 100) // 70
places_length = (w * 100) // 120
total_places = places_width * places_length - 3
total = int(total_places)
print(total)

