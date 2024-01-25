'''# Read user input
user = input()
pwd = input()
user_input = input()
# Logic
while user_input != pwd:
    user_input = input()


# Output
print(f'Welcome {user}!')'''

user = input()
pwd = input()

# Logic
while True:
    user_input = input()
    if user_input == pwd:
        break


# Output
print(f'Welcome {user}!')