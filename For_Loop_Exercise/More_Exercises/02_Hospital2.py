def treat_patients_on_day(count_patient, count_doctor):
    if count_patient <= count_doctor:
        treated_patients_per_day = count_patient
        untreated_patients_per_day = 0
    else:
        treated_patients_per_day = count_doctor
        untreated_patients_per_day = count_patient - treated_patients_per_day

    return treated_patients_per_day, untreated_patients_per_day


n = int(input())
count_doctor = 7
sum_treated_patients = 0
sum_untreated_patients = 0

for i in range(1, n + 1):
    count_patient = int(input())

    if i % 3 == 0 and sum_untreated_patients > sum_treated_patients:
        count_doctor += 1

    treated_patients_per_day, untreated_patients_per_day = treat_patients_on_day(count_patient, count_doctor)
    sum_treated_patients += treated_patients_per_day
    sum_untreated_patients += untreated_patients_per_day

print(f"Treated patients: {sum_treated_patients}.")
print(f"Untreated patients: {sum_untreated_patients}.")