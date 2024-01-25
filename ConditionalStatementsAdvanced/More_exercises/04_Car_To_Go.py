budget = float(input())
season = input()

if budget <= 100:
    print("Economy class")
    if season == "Summer":
        print(f"Cabrio - {0.35 * budget:.2f}")
    elif season == "Winter":
        print(f"Jeep - {0.65 * budget:.2f}")
elif 100 < budget <= 500:
    print("Compact class")
    if season == "Summer":
        print(f"Cabrio - {0.45 * budget:.2f}")
    elif season == "Winter":
        print(f"Jeep - {0.80 * budget:.2f}")
else:
    print("Luxury class")
    print(f"Jeep - {0.90 * budget:.2f}")