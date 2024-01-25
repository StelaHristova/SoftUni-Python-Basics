n = input()

count_c, count_o, count_n = 0, 0, 0

is_ready = False
message = ''
word = ''
while n != 'End':
    if chr(65) <= n <= chr(90) or chr(97) <= n <= chr(122):
        if n == 'c':
            count_c += 1
            if count_c > 1:
                word += n
        elif n == 'o':
            count_o += 1
            if count_o > 1:
                word += n
        elif n == 'n':
            count_n += 1
            if count_n > 1:
                word += n
        else:
            word += n

        if count_o >= 1 and count_n >= 1 and count_c >= 1:
            message += word + ' '
            count_c, count_o, count_n = 0, 0, 0
            word = ''

    n = input()

if n == 'End':
    is_ready = True
    print(message)

# if n.isalpha()