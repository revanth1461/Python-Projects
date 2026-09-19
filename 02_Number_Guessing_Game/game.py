import random
ATTEMPTS = 7
def show_rules():
    print("Welcome to Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it.\n")
def play_game(number):
    attempt = 1
    while attempt <= ATTEMPTS:
        guess = input(f"Attempt {attempt}/7 - Enter your guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.\n")
            continue
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.\n")
            continue
        if guess == number:
            print("\nCongratulations!")
            print("You guessed the correct number.")
            print("Attempts used:", attempt)
            return
        elif guess < number:
            print("Too Low! Try a higher number.\n")
        else:
            print("Too High! Try a lower number.\n")
        attempt += 1
    print("\nGame Over!")
    print("The correct number was:", number)
show_rules()
random_number = random.randint(1, 100)
play_game(random_number)