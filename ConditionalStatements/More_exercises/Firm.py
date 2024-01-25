import math

project_hours = int(input())
available_days = int(input())
workers = int(input())

work_days = 0.90 * available_days
overtime_hours = work_days * 2 * workers
work_hours = work_days * 8 * workers + overtime_hours

if work_hours >= project_hours:
    print("Yes!{0} hours left.".format(math.floor(abs(project_hours - work_hours))))
else:
    print("Not enough time!{0} hours needed.".format(math.floor(abs(work_hours - project_hours))))