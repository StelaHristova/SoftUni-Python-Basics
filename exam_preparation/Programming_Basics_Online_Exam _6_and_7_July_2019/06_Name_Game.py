first_points = 0
second_points = 0
winners_name = ''

while True:
    name = input()
    second_points = 0
    if name == 'Stop':
        break

    for i in range(0, len(name)):
        guess = int(input())
        num = ord(name[i])
        if guess == num:
            second_points += 10
        else:
            second_points += 2

    if second_points >= first_points:
        winners_name = name
        first_points = second_points

print(f'The winner is {winners_name} with {first_points} points!')

