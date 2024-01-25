holidays = int(input())
import math
working_days = 365 - holidays
total_play_minutes = working_days * 63 + holidays * 127

difference = math.fabs(total_play_minutes - 30000)
hours = difference // 60
minutes = difference % 60

if total_play_minutes >= 30000:
    print("Tom will run away")
    print(f"{hours:.0f} hours and {minutes:.0f} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours:.0f} hours and {minutes:.0f} minutes less for play")