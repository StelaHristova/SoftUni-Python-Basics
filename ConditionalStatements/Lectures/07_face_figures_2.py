figure_name = input()
is_figure_name_valid = False

if figure_name == "square":
   is_figure_name_valid = True
   a = float(input())
   area = a * a
elif figure_name == "rectangle":
   is_figure_name_valid = True
   a = float(input())
   b = float(input())
   area = a * b
elif figure_name == "circle":
   is_figure_name_valid = True
   r = float(input())
   from math import pi
   area = pi * r * r
elif figure_name == "triangle":
   is_figure_name_valid = True
   a = float(input())
   h = float(input())
   area = a * h / 2

if is_figure_name_valid:
   print(f"The figure is {figure_name} with area of {area:.3f} sq.cm")