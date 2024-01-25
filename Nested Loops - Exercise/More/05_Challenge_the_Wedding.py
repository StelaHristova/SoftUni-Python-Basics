count_men = int(input())
count_women = int(input())
max_tables = int(input())
tables = 0
for i in range(1, count_men + 1):
    for j in range(1, count_women + 1):
        tables += 1
        if tables > max_tables:
            break
        print(f'({i} <-> {j})', end= ' ')