price_skumriq_kg = float (input())
price_caca_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

price_palamud = price_skumriq_kg + price_skumriq_kg * 60 / 100
sum_palamud = price_palamud * palamud_kg
price_safrid = price_caca_kg + price_caca_kg * 80 / 100
sum_safrid = price_safrid * safrid_kg
sum_midi = midi_kg * 7.5
sum = sum_palamud + sum_safrid + sum_midi
total_sum = "{:.2f}".format(sum)

print(total_sum)