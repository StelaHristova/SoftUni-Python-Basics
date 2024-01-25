# First solution
# start_num = int(input())
# end_num = int(input())
#
# for i in range(start_num, end_num + 1):
#     current_num_str = str(i)
#     even_sum = 0
#     odd_sum = 0
#     for symbol_count in range(0, len(current_num_str)):
#         digit = int(current_num_str[symbol_count])
#         if symbol_count % 2 == 0:
#             odd_sum += digit
#         else:
#             even_sum += digit
#     if even_sum == odd_sum:
#         print(current_num_str, end=' ')

# # Second solution
#
# start_num = int(input())
# end_num = int(input())
#
# for i in range(start_num, end_num + 1):
#     current_num = i
#     counter = len(str(current_num))
#     even_sum = 0
#     odd_sum = 0
#     while counter > 0:
#         digit = current_num % 10
#         if counter % 2 == 0:
#             even_sum += digit
#         else:
#             odd_sum += digit
#         current_num = current_num // 10
#         counter -= 1
#
#     if even_sum == odd_sum:
#         print(i, end=' ')

# Third solution
import math
start_num = int(input())
end_num = int(input())

for i in range(start_num, end_num + 1):
    current_num = i
    even_sum = 0
    odd_sum = 0
    # counter = math.floor(math.log10(current_num) + 1)
    # Forth solution
    # counter = 0
    # while current_num != 0:
    #     current_num //= 10
    #     counter += 1
    # current_num = i

    while counter > 0:
        digit = current_num % 10
        if counter % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        current_num = current_num // 10
        counter -= 1

    if even_sum == odd_sum:
        print(i, end=' ')
