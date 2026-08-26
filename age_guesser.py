import random

def main():
    print("Welcome to the Age Guesser!")
    name = input("Please enter your name: ")
    guess = random.randint(15, 41)
    guess_count = 0
    while name:
        guess_count += 1
        print(f"Is it your age {guess}?")
        response = input("Please answer with 'yes' or 'no': ").strip().lower()
        if response == 'yes':
            print(f"Great! Your name is {name} and your age is {guess}.")
            print(f"It took me {guess_count} guesses.")
            break

        elif guess_count >= 5:
            print(f"\nI give up! I couldn't guess your age in 5 tries.")
            break

        else:
            print(f"\nRats. I will try to guess again!\n")
            guess = random.randint(15, 41)
            
    else:
        print("Invalid input. Please enter your name.")

if __name__ == "__main__":
    main()