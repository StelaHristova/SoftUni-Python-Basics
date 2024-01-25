wished_height = int(input())
current_height = wished_height - 30
count_success = 0
count_fails = 0

while True:
    jump_height = int(input())
    count_fails += 1

    if jump_height > current_height:
        current_height += 5
        count_fails = 0
        count_success += 1
        if current_height > wished_height:
            break
    if count_fails == 3:
        break

if current_height > wished_height:
    print(f'Tihomir succeeded, he jumped over {wished_height}cm after {count_fails + count_success} jumps.')
else:
    print(f'Tihomir failed at {current_height}cm after {count_fails + count_success} jumps.')

