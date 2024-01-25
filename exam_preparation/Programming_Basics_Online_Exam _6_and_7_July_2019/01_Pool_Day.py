from math import ceil
import math
count_people = int(input())
tax_entrance = float(input())
price_for_one_sunbed = float(input())
price_for_one_umbrella = float(input())

tax_entrance_all_people = count_people * tax_entrance
tax_sunbeds = (math.ceil(0.75 * count_people)) * price_for_one_sunbed
tax_umbrellas = (math.ceil(0.50 * count_people)) * price_for_one_umbrella
total_tax = tax_entrance_all_people + tax_umbrellas + tax_sunbeds
print(f'{total_tax:.2f} lv.')
