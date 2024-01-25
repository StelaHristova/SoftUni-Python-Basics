n = int(input())
treated_patients_per_day = 0
untreated_patients_per_day = 0
sum_treated_patients = 0
sum_untreated_patients = 0
count_doctor = 7

for i in range(1, n + 1):
    count_patient = int(input())

    if i % 3 != 0:
        if count_patient <= count_doctor:
            treated_patients_per_day = count_patient
            sum_treated_patients += treated_patients_per_day
        else:
            treated_patients_per_day = count_doctor
            untreated_patients_per_day = count_patient - treated_patients_per_day
            sum_treated_patients += treated_patients_per_day
            sum_untreated_patients += untreated_patients_per_day
    else:
        if sum_untreated_patients > sum_treated_patients:
            count_doctor += 1
            if count_patient <= count_doctor:
                treated_patients_per_day = count_patient
                sum_treated_patients += treated_patients_per_day
            else:
                treated_patients_per_day = count_doctor
                untreated_patients_per_day = count_patient - treated_patients_per_day
                sum_treated_patients += treated_patients_per_day
                sum_untreated_patients += untreated_patients_per_day
        else:
            if count_patient <= count_doctor:
                treated_patients_per_day = count_patient
                sum_treated_patients += treated_patients_per_day
            else:
                treated_patients_per_day = count_doctor
                untreated_patients_per_day = count_patient - treated_patients_per_day
                sum_treated_patients += treated_patients_per_day
                sum_untreated_patients += untreated_patients_per_day



print(f"Treated patients: {sum_treated_patients}.")
print(f"Untreated patients: {sum_untreated_patients}.")
