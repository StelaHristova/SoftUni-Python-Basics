n = int(input())
total_sum_current = 0
total_sum_previous = 0
diff = 0
max_diff = 0

for i in range(n):
    num1 = int(input())
    num2 = int(input())
    total_sum_current = num1 + num2
    if total_sum_current > total_sum_previous:
        diff = total_sum_current - total_sum_previous
    else:
        diff = total_sum_previous - total_sum_current
    total_sum_previous = total_sum_current
    if i != 0:
        if diff > max_diff:
            max_diff = diff
if n == 1:
    diff = 0

if diff == 0:
   print(f"Yes, value={total_sum_current}")
else:
    print(f"No, maxdiff={max_diff}")
