n = int(input())
l = int(input())

new_l = ord('a') + l
for a1 in range(1, n + 1):
    for a2 in range(1, n + 1):
        for a3 in range(ord('a'), new_l):
            a3 = chr(a3)
            for a4 in range(ord('a'), new_l):
                a4 = chr(a4)
                for a5 in range(1, n + 1):
                    if a5 > a1 and a5 > a2:

                        print(f'{a1}{a2}{a3}{a4}{a5}', end=' ')
