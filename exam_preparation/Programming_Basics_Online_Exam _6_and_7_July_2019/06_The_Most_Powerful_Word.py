import math
most_powerful_word = ''
max_power = 0

while True:
    word = input()
    if word == 'End of words':
        break

    power = sum(ord(i) for i in word)

    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y' or \
            word[0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] == 'U' or word[0] == 'Y':
        power *= len(word)
    else:
        power /= len(word)

    if power > max_power:
        max_power = power
        most_powerful_word = word

print(f'The most powerful word is {most_powerful_word} - {math.floor(max_power)}')
