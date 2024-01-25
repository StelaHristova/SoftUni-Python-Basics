name_football_team = input()
count_play_games = int(input())
count_win_games = 0
count_equal_games = 0
count_lost_games = 0
points = 0

for i in range(count_play_games):
    result = input()

    if result == 'W':
        count_win_games += 1
        points += 3
    elif result == 'D':
        count_equal_games += 1
        points += 1
    elif result == 'L':
        count_lost_games += 1

if count_play_games == 0:
    print(f"{name_football_team} hasn't played any games during this season.")
else:
    print(f'{name_football_team} has won {points} points during this season.')
    print(f'Total stats:')
    print(f'## W: {count_win_games}')
    print(f'## D: {count_equal_games}')
    print(f'## L: {count_lost_games}')
    print(f'Win rate: {count_win_games / count_play_games * 100:.2f}%')