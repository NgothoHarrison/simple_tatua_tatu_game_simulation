# tatua tatu simulation
# it's a gambling experience the asks the user to guess three lucky winning numbers
# and award them accordingly in conditions
# if the user inputs and the three generated numbers match perfectly, they win a mega price of 1,000,000
# if two numbers match, a win of 500,000
# if one number match, a win of 100,000
# /// NOTE, the number positions should align in position

import random


def generate_numbers():
    return [random.randint(2, 50) for _ in range(3)]


def main():
    print("Welcome to Tatua Tatu!")
    user_name = input("Enter your name: ")

    # Generate three random numbers
    generated_numbers = generate_numbers()

    print("Today's three winning numbers are between 2 and 50. Match them and win a great reward!")

    user_guesses = []
    for i in range(3):
        guess = int(input(f"Enter your guess for position {i + 1} (between 2 and 50): "))
        user_guesses.append(guess)

    print(f"\nThe winning numbers were: {generated_numbers}")
    print(f"Your guesses were: {user_guesses}")

    # Check for matches and determine the prize
    match_count = sum(g == u for g, u in zip(generated_numbers, user_guesses))

    if match_count == 3:
        print(f"Congratulations, {user_name}! You've won the mega prize of 1,000,000!")
    elif match_count == 2:
        print(f"Congratulations, {user_name}! You've won 500,000!")
    elif match_count == 1:
        print(f"Congratulations, {user_name}! You've won 100,000!")
    else:
        print(f"Sorry, {user_name}, better luck next time. Keep trying.")


if __name__ == "__main__":
    main()
