import random

x_number = random.randint(1, 10)
attempts = 5

print(f"(Debug: the number is {x_number})")  # Remove this line in real game

for remaining in range(attempts, 0, -1):
    print(f"Guess a number between 1 and 10. You have {remaining} attempts left.")
    try:
        guess = int(input("> "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess < x_number:
        print("Your guess is too low.")
    elif guess > x_number:
        print("Your guess is too high.")
    else:
        print("Correct!")
        break
else:  # Executes only if the loop wasn't broken
    print(f"You failed, the solution was {x_number}.")

    # For README: f-strings (f"Hello {name}") are concise, readable, and the most professional and good practice choice.
