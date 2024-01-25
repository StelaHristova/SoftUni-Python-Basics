import math

n_count_days = int(input())
m_km_first_day = float(input())
total_km = m_km_first_day
for i in range(2, n_count_days + 2):
    percentage = int(input())
    km_next_day = m_km_first_day * ((percentage)/ 100 + 1)
    total_km += km_next_day
    m_km_first_day = km_next_day

if total_km >= 1000:
    print(f"You've done a great job running {math.ceil(total_km - 1000)} more kilometers!")
else:
    print(f'Sorry Mrs. Ivanova, you need to run {math.ceil(1000 - total_km)} more kilometers')