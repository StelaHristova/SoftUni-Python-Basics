count_students_total = int(input())

count_students5, count_students4, count_students3, count_students2 = 0, 0, 0, 0
average = 0
for i in range(count_students_total):
    grade_exam = float(input())
    average += grade_exam / count_students_total
    if grade_exam >= 5:
        count_students5 += 1
    elif 4 <= grade_exam <= 4.99:
        count_students4 += 1
    elif 3 <= grade_exam <= 3.99:
        count_students3 += 1
    else:
        count_students2 += 1
print(f"Top students: {count_students5 * 100 / count_students_total:.2f}%")
print(f"Between 4.00 and 4.99: {count_students4 * 100 / count_students_total:.2f}%")
print(f"Between 3.00 and 3.99: {count_students3 * 100 / count_students_total:.2f}%")
print(f"Fail: {count_students2 * 100 / count_students_total:.2f}%")
print(f"Average: {average:.2f}")
