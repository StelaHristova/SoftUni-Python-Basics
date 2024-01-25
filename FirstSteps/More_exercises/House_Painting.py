x = float(input())
y = float(input())
h = float(input())

side_wall = x * y
window = 1.5 * 1.5
door = 1.2 * 2
front_wall = x * x
area = 2 * side_wall - 2 * window + 2 * front_wall - door
green_paint = area / 3.4
green = "{:.2f}".format(green_paint)
print(green)
roof_rect = x * y
roof_triangle = (x * h) / 2
area_roof = 2 * roof_rect + 2 * roof_triangle
red_paint = area_roof / 4.3
red = "{:.2f}".format(red_paint)
print(red)