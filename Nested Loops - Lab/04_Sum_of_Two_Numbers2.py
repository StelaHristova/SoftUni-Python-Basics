start_num, end_num = int(input()), int(input())
magic_number = int(input())

for first_num in range(start_num, end_num + 1):
    for second_num in range(start_num, end_num + 1):
        if first_num + second_num == magic_number:
            combinations = (first_num - start_num) * (end_num - start_num + 1) + (second_num - start_num + 1)
            print(f'Combination N:{combinations} ({first_num} + {second_num} = {magic_number})')
            exit()

combinations = (end_num - start_num + 1) ** 2

print(f'{combinations} combinations - neither equa ls {magic_number}')