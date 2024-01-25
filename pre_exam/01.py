count_people = int(input())
count_nights = int(input())
count_cards_for_transport = int(input())
count_tickets_for_museum = int(input())

price_nights = 20 * count_nights
price_cads_for_transport = count_cards_for_transport * 1.60
price_museum_tickets = count_tickets_for_museum * 6
total_sum = (price_nights + price_cads_for_transport + price_museum_tickets) * count_people * 1.25

print(f'{total_sum:.2f}')