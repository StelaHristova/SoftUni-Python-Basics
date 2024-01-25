season = input()
type_group = input()
count_students = int(input())
count_per_night = int(input())

if count_students >= 50:
    if type_group == "boys":
        if season == "Winter":
            print(f"Judo {(count_students * 9.60 * count_per_night * 0.50):.2f} lv.")
        if season == "Spring":
            print(f"Tennis {(count_students * 7.20 * count_per_night * 0.50):.2f} lv.")
        if season == "Summer":
            print(f"Football {(count_students * 15 * count_per_night * 0.50):.2f} lv.")
    elif type_group == "girls":
        if season == "Winter":
            print(f"Gymnastics {(count_students * 9.60 * count_per_night * 0.50):.2f} lv.")
        if season == "Spring":
            print(f"Athletics {(count_students * 7.20 * count_per_night * 0.50):.2f} lv.")
        if season == "Summer":
            print(f"Volleyball {(count_students * 15 * count_per_night * 0.50):.2f} lv.")
    elif type_group == "mixed":
        if season == "Winter":
            print(f"Ski {(count_students * 10 * count_per_night * 0.50):.2f} lv.")
        if season == "Spring":
            print(f"Cycling {(count_students * 9.50 * count_per_night * 0.50):.2f} lv.")
        if season == "Summer":
            print(f"Swimming {(count_students * 20 * count_per_night * 0.50):.2f} lv.")
elif 20 <= count_students < 50:
    if type_group == "boys":
        if season == "Winter":
            print(f"Judo {(count_students * 9.60 * count_per_night * 0.85):.2f} lv.")
        if season == "Spring":
            print(f"Tennis {(count_students * 7.20 * count_per_night * 0.85):.2f} lv.")
        if season == "Summer":
            print(f"Football {(count_students * 15 * count_per_night * 0.85):.2f} lv.")
    elif type_group == "girls":
        if season == "Winter":
            print(f"Gymnastics {(count_students * 9.60 * count_per_night * 0.85):.2f} lv.")
        if season == "Spring":
            print(f"Athletics {(count_students * 7.20 * count_per_night * 0.85):.2f} lv.")
        if season == "Summer":
            print(f"Volleyball {(count_students * 15 * count_per_night * 0.85):.2f} lv.")
    elif type_group == "mixed":
        if season == "Winter":
            print(f"Ski {(count_students * 10 * count_per_night * 0.85):.2f} lv.")
        if season == "Spring":
            print(f"Cycling {(count_students * 9.50 * count_per_night * 0.85):.2f} lv.")
        if season == "Summer":
            print(f"Swimming {(count_students * 20 * count_per_night * 0.85):.2f} lv.")
elif 10 <= count_students < 20:
    if type_group == "boys":
        if season == "Winter":
            print(f"Judo {(count_students * 9.60 * count_per_night * 0.95):.2f} lv.")
        if season == "Spring":
            print(f"Tennis {(count_students * 7.20 * count_per_night * 0.95):.2f} lv.")
        if season == "Summer":
            print(f"Football {(count_students * 15 * count_per_night * 0.95):.2f} lv.")
    elif type_group == "girls":
        if season == "Winter":
            print(f"Gymnastics {(count_students * 9.60 * count_per_night * 0.95):.2f} lv.")
        if season == "Spring":
            print(f"Athletics {(count_students * 7.20 * count_per_night * 0.95):.2f} lv.")
        if season == "Summer":
            print(f"Volleyball {(count_students * 15 * count_per_night * 0.95):.2f} lv.")
    elif type_group == "mixed":
        if season == "Winter":
            print(f"Ski {(count_students * 10 * count_per_night * 0.95):.2f} lv.")
        if season == "Spring":
            print(f"Cycling {(count_students * 9.50 * count_per_night * 0.95):.2f} lv.")
        if season == "Summer":
            print(f"Swimming {(count_students * 20 * count_per_night * 0.95):.2f} lv.")
else:
    if type_group == "boys":
        if season == "Winter":
            print(f"Judo {(count_students * 9.60 * count_per_night):.2f} lv.")
        if season == "Spring":
            print(f"Tennis {(count_students * 7.20 * count_per_night):.2f} lv.")
        if season == "Summer":
            print(f"Football {(count_students * 15 * count_per_night):.2f} lv.")
    elif type_group == "girls":
        if season == "Winter":
            print(f"Gymnastics {(count_students * 9.60 * count_per_night):.2f} lv.")
        if season == "Spring":
            print(f"Athletics {(count_students * 7.20 * count_per_night):.2f} lv.")
        if season == "Summer":
            print(f"Volleyball {(count_students * 15 * count_per_night):.2f} lv.")
    elif type_group == "mixed":
        if season == "Winter":
            print(f"Ski {(count_students * 10 * count_per_night):.2f} lv.")
        if season == "Spring":
            print(f"Cycling {(count_students * 9.50 * count_per_night):.2f} lv.")
        if season == "Summer":
            print(f"Swimming {(count_students * 20 * count_per_night):.2f} lv.")