count_sale_games = int(input())
sale_Hearthstone = 0
sale_Fornite = 0
sale_Overwatch = 0
sale_Others = 0
total_sale = 0
for i in range(count_sale_games):
    name_games = input()

    if name_games == 'Hearthstone':
        sale_Hearthstone += 1
    elif name_games == 'Fornite':
        sale_Fornite += 1
    elif name_games == 'Overwatch':
        sale_Overwatch += 1
    else:
        sale_Others += 1
total_sale = sale_Hearthstone + sale_Fornite + sale_Overwatch + sale_Others
print(f'Hearthstone - {(sale_Hearthstone / total_sale) * 100:.2f}%')
print(f'Fornite - {(sale_Fornite / total_sale) * 100:.2f}%')
print(f'Overwatch - {(sale_Overwatch / total_sale) * 100:.2f}%')
print(f'Others - {(sale_Others / total_sale) * 100:.2f}%')
