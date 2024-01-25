last_sector = input()
count_rows_first_sector = int(input())
count_places_odd_row = int(input())

num_sector = ord(last_sector)
counter = 0
for sector in range(65, num_sector + 1):
    if sector != 65:
        count_rows_first_sector += 1
    for row in range(1, count_rows_first_sector + 1):
        if row % 2 != 0:
            for place in range(97, 97 + count_places_odd_row):
                counter += 1
                print(f'{chr(sector)}{row}{chr(place)}')
        else:
            for place in range(97, 97 + count_places_odd_row + 2):
                counter += 1
                print(f'{chr(sector)}{row}{chr(place)}')
print(counter)