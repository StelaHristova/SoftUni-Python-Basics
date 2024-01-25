n = int(input())
odd_sum = 0
odd_min = None
odd_max = None
even_sum = 0
even_min = None
even_max = None

for i in range(n):
    num = float(input())
    if (i - 1) % 2 == 0:
        even_sum += num
        if even_max is None or num > even_max:
            even_max = num
        if even_min is None or num < even_min:
            even_min = num
    else:
        odd_sum += num
        if odd_max is None or num > odd_max:
            odd_max = num
        if odd_min is None or num < odd_min:
            odd_min = num

print(f"OddSum={odd_sum:g},")

if odd_min is None:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:g},")

if odd_max is None:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:g},")

print(f"EvenSum={even_sum:g},")

if even_min is None:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:g},")

if even_max is None:
    print(f"EvenMax=No,")
else:
    print(f"EvenMax={even_max:g}")





