num = input()
n_of_num = len(num)

third_number_str = (num[0])
third_number = int(third_number_str)
second_number_str = (num[1])
second_number = int(second_number_str)
first_number_str = (num[2])
first_number = int(first_number_str)

for i in range(1, first_number + 1):
    for j in range(1, second_number + 1):
        for k in range(1, third_number + 1):
            print(f'{i} * {j} * {k} = {k * j * i};')



