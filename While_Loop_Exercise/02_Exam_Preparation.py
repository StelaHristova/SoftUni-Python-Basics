poor_grades = int(input())

input_line = input()
sum_grades = 0
count_grades = 0
last_problem = ''
poor_grades_count = 0

while input_line != 'Enough':
    last_problem = input_line
    current_grades = int(input())
    if current_grades <= 4:
        poor_grades_count += 1
    sum_grades += current_grades
    count_grades += 1

    if poor_grades_count >= poor_grades:
        break

    input_line = input()

if poor_grades_count == poor_grades:
    print(f'You need a break, {poor_grades_count} poor grades.')
else:
    print(f'Average score: {sum_grades / count_grades:.2f}')
    print(f'Number of problems: {count_grades}')
    print(f'Last problem: {last_problem}')