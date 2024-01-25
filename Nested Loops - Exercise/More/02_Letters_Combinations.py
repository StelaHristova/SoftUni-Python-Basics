letter1 = input()
letter2 = input()
letter3 = input()
is_valid = False

# 97 = 'a , 122 = 'z'
num_1 = ord(letter1)
num_2 = ord(letter2)
num_3 = ord(letter3)

combination = 0

for i in range(num_1, num_2 + 1):
    for j in range(num_1, num_2 + 1):
        for k in range(num_1, num_2 + 1):
            is_valid = k == num_3 or j == num_3 or i == num_3
            if is_valid:
                pass
            else:
                combination += 1
                print(chr(i) + chr(j) + chr(k), end=" ")

print(combination)

