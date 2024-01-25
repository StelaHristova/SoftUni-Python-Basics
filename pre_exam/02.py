price_t_shirt = float(input())
sum_to_win = float(input())

price_shorts = 0.75 * price_t_shirt
price_socks = 0.20 * price_shorts
price_shoes = 2 * (price_t_shirt + price_shorts)
total_sum = 0.85 * (price_t_shirt + price_shorts + price_socks + price_shoes)

if total_sum >= sum_to_win:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_sum:.2f} lv.')
else:
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {abs(total_sum - sum_to_win):.2f} lv. more.')