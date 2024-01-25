a = int(input())
b = int(input())
max_count_generated_passwords = int(input())
counter = 0

A = 35
B = 64

passwords = ''
current_password = ''
while counter < max_count_generated_passwords:
    x = 1
    while x <= a and counter < max_count_generated_passwords:
        y = 1
        while y <= b and counter < max_count_generated_passwords:
            current_password = chr(A) + chr(B) + str(x) + str(y) + chr(B) + chr(A)
            passwords += current_password + '|'
            counter += 1
            y += 1
            B += 1
            if B > 96:
                B = 64

            A += 1
            if A > 55:
                A = 35
        x += 1
    if counter == max_count_generated_passwords or x > a or y > b:
        break

print(passwords, end='')
# for i in range(35, 56):
#     counter += 1
#
#     for j in range(64, 97):
#         for k in range(1, a + 1):
#             for l in range(1, b + 1):
#                 for m in range(64, 97):
#                     for n in range(35, 56):
#                         if counter > max_count_generated_passwords:
#                             break
#                         if k == a or l == b:
#                             break
#
#                         print(f'{chr(i)}{chr(j)}{k}{l}{chr(m)}{chr(n)}|', end='')
