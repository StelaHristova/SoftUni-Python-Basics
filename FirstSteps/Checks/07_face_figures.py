figure_name = str (input())

if figure_name == "square":
   a = float(input())
   area = a * a
   print(round(area, 3))
elif figure_name == "rectangle":
   a = float(input())
   b = float(input())
   area = a * b
   print(round(area, 3))
elif figure_name == "circle":
   r = float(input())
   from math import pi
   area = pi * r * r
   print(round(area, 3))
elif figure_name == "triangle":
   a = float(input())
   h = float(input())
   area = a * h / 2
   print(round(area, 3))