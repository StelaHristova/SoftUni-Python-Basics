deposit_sum = float(input())
deposit_term = int(input())
year_discount_rate = float(input())
total_sum = deposit_sum + deposit_term * ((deposit_sum * year_discount_rate / 100) / 12 )

print((total_sum))