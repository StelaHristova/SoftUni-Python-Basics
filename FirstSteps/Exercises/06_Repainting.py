nylon = int(input())
paint = int(input())
paint_thinner = int(input())
worker_hours = int(input())

fixed_price_nylon = 1.50
fixed_price_paint = 14.50
fixed_price_paint_thinner = 5.00
price_bags = 0.40

sum_nylon = (nylon + 2) * fixed_price_nylon
sum_paint = (paint + (paint * 10 / 100)) * fixed_price_paint
sum_paint_thinner = paint_thinner * fixed_price_paint_thinner
total_sum = sum_nylon + sum_paint + sum_paint_thinner + price_bags
total_sum_workers = (total_sum * 30 / 100) * worker_hours
end_sum = total_sum + total_sum_workers

print (end_sum)