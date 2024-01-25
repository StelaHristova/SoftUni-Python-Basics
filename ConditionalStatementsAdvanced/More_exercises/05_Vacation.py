budget = float(input())
season = input()

if budget <= 1000:
    if season == "Summer":
        print(f"Alaska - Camp - {0.65 * budget:.2f}")
    if season == "Winter":
        print(f"Morocco - Camp - {0.45 * budget:.2f}")
elif 1000 < budget <= 3000:
    if season == "Summer":
        print(f"Alaska - Hut - {0.80 * budget:.2f}")
    if season == "Winter":
        print(f"Morocco - Hut - {0.60 * budget:.2f}")
else:
    if season == "Summer":
        print(f"Alaska - Hotel - {0.90 * budget:.2f}")
    if season == "Winter":
        print(f"Morocco - Hotel - {0.90 * budget:.2f}")