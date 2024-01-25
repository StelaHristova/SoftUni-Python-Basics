kg_vegetables = float(input())
kg_fruits = float(input())
all_kg_vegetables = int(input())
all_kg_fruits = int(input())

sum_vegetables = kg_vegetables * all_kg_vegetables
sum_fruits = kg_fruits * all_kg_fruits
total_sum = (sum_vegetables + sum_fruits) / 1.94
final_sum = "{:.2f}".format(total_sum)

print(final_sum)