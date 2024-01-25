figure_name = input()

if figure_name == "square":
   a = float(input())
   area = a * a
   print(f"{area:.3f}")
elif figure_name == "rectangle":
   a = float(input())
   b = float(input())
   area = a * b
   print(f"{area:.3f}")
elif figure_name == "circle":
   r = float(input())
   from math import pi
   area = pi * r * r
   print(f"{area:.3f}")
elif figure_name == "triangle":
   a = float(input())
   h = float(input())
   area = a * h / 2
   print(f"{area:.3f}")