count_groups = int(input())
total_people = 0

climbers_5 = 0
climbers_6_12 = 0
climbers_13_25 = 0
climbers_26_40 = 0
climbers_41 = 0
for i in range(count_groups):
    count_people_in_group = int(input())
    total_people += count_people_in_group

    if count_people_in_group <= 5:
        climbers_5 += count_people_in_group
    elif 6 <= count_people_in_group <= 12:
        climbers_6_12 += count_people_in_group
    elif 13 <= count_people_in_group <= 25:
        climbers_13_25 += count_people_in_group
    elif 26 <= count_people_in_group <= 40:
        climbers_26_40 += count_people_in_group
    elif count_people_in_group >= 41:
        climbers_41 += count_people_in_group


print(f"{climbers_5 / total_people * 100:.2f}%")
print(f"{climbers_6_12 / total_people * 100:.2f}%")
print(f"{climbers_13_25 / total_people * 100:.2f}%")
print(f"{climbers_26_40 / total_people * 100:.2f}%")
print(f"{climbers_41 / total_people * 100:.2f}%")