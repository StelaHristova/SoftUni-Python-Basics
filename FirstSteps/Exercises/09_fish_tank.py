lenght_cm = int(input())
width_cm = int(input())
height_cm = int(input())
procent = float(input())

volume_cm = lenght_cm * width_cm * height_cm
volume_l = volume_cm / 1000
used_volume = procent / 100
required_l = volume_l * (1 - used_volume)

print(required_l)