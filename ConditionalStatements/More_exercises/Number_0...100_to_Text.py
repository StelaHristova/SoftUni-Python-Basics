number = int(input())

if number < 0 or number > 100:
    print("invalid number")
elif number < 20:
    if number == 0:
        print("zero")
    elif number == 1:
       print("one")
    elif number == 2:
       print("two")
    elif number == 3:
       print("three")
    elif number == 4:
       print("four")
    elif number == 5:
       print("five")
    elif number == 6:
       print("six")
    elif number == 7:
       print("seven")
    elif number == 8:
       print("eight")
    elif number == 9:
       print("nine")
    elif number == 10:
       print("ten")
    elif number == 11:
       print("eleven")
    elif number == 12:
       print("twelve")
    elif number == 13:
       print("thirteen")
    elif number == 14:
       print("fourteen")
    elif number == 15:
       print("fifteen")
    elif number == 16:
       print("sixteen")
    elif number == 17:
       print("seventeen")
    elif number == 18:
       print("eighteen")
    elif number == 19:
       print("nineteen")
elif 20 <= number < 100:
    left_part = number // 10
    right_part = number % 10
    if left_part == 2:
      left_part = "twenty"
    elif left_part == 3:
       left_part = "thirty"
    elif left_part == 4:
       left_part = "forty"
    elif left_part == 5:
       left_part = "fifty"
    elif left_part == 6:
       left_part = "sixty"
    elif left_part == 7:
       left_part = "seventy"
    elif left_part == 8:
       left_part = "eighty"
    elif left_part == 9:
       left_part = "ninety"

    if right_part == 0:
        print("{}".format(left_part))
    else:
        if right_part == 1:
            right_part = "one"
        elif right_part == 2:
            right_part = "two"
        elif right_part == 3:
            right_part = "three"
        elif right_part == 4:
            right_part = "four"
        elif right_part == 5:
            right_part = "five"
        elif right_part == 6:
            right_part = "six"
        elif right_part == 7:
            right_part = "seven"
        elif right_part == 8:
            right_part = "eight"
        elif right_part == 9:
            right_part = "nine"
        print("{} {}".format(left_part, right_part))
elif number == 100:
    print("one hundred")