import math

name_tv_show = input()
duration_episode = int(input())
duration_brake = int(input())

lunch_time = 1 / 8 * duration_brake
relax_time = 1/4 * duration_brake
left_time = duration_brake - lunch_time - relax_time

total_time = math.ceil(abs(duration_episode - left_time))

if left_time >= duration_episode:
    print(f"You have enough time to watch {name_tv_show} and left with {total_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_tv_show}, you need {abs(total_time)} more minutes.")