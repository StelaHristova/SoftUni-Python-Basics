best_player =''
is_het_trick = False
win_goals = 0
while True:
    player_name = input()

    if player_name == "END":
        break

    count_goals = int(input())
    if win_goals < count_goals:
        win_goals = count_goals
        best_player = player_name
        if win_goals >= 3:
            is_het_trick = True
            if win_goals >= 10:
                break

print(f'{best_player} is the best player!')
if is_het_trick:
    print(f'He has scored {win_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {win_goals} goals.')

