count_juniors = int(input())
count_seniors = int(input())
type_track = input()

juniors_trail = 5.50
juniors_cross_country = 8
juniors_downhill = 12.25
juniors_road = 20
seniors_trail = 7
seniors_cross_country = 9.50
seniors_downhill = 13.75
seniors_road = 21.50

if type_track == "trail":
    sum_juniors = count_juniors * juniors_trail
    sum_seniors = count_seniors * seniors_trail
elif type_track == "cross-country":
    sum_juniors = count_juniors * juniors_cross_country
    sum_seniors = count_seniors * seniors_cross_country
elif type_track == "downhill":
    sum_juniors = count_juniors * juniors_downhill
    sum_seniors = count_seniors * seniors_downhill
else:
    sum_juniors = count_juniors * juniors_road
    sum_seniors = count_seniors * seniors_road

total_sum = sum_juniors + sum_seniors

if type_track == "cross-country" and (count_seniors + count_juniors) >= 50:
    total_sum *= 0.75

expenses = total_sum * 5 / 100
print(f"{total_sum - expenses:.2f}")
