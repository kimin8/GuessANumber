import random

level = 1

while level <= 5:
    upper_boundary = level * 100
    computer_choice = random.randint(1, upper_boundary)
    print(f'Level {level}: Guess the number (1-{upper_boundary})')
    player_guess = input()
    attemps = 0

    while True:
        player_guess = int(player_guess)
        attemps += 1

        if player_guess == computer_choice:
            print(f"You guessed it in {attemps} tries! Congratulations!")
            break;
        elif player_guess > computer_choice and player_guess <= upper_boundary:
            print("Too high! Try again...")
        elif player_guess < computer_choice and player_guess >= 1:
            print("Too low! Try again...")
        else:
            raise SystemExit("Invalid input! The game crashed! Please restart...")

        player_guess = input()
    level += 1

print("Congratulations! You have completed the final level! From now on, I shall call you 'THE KING OF GUESSING'!")