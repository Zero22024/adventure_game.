import time
import random


def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()


def start_game():
    print_slow("Welcome to the Adventure!")
    print_slow("You find yourself in a dark forest...")
    print_slow("You can see two paths ahead of you.")


def choose_path():
    print_slow("Which path will you choose? (left/right)")
    while True:
        choice = input().lower()
        if choice == 'left' or choice == 'right':
            return choice
        else:
            print_slow("Invalid choice. Please enter 'left' or 'right'.")


def explore_path(path):
    if path == 'left':
        print_slow("You encounter a pack of wolves!")
        if random.choice([True, False]):
            print_slow("You defeat the wolves and find a treasure chest!")
            return True
        else:
            print_slow("The wolves overpower you. Game Over!")
            return False
    else:
        print_slow("You come across a peaceful meadow.")
        print_slow("You find a friendly traveler who gives you a map.")
        return True


def play_again():
    print_slow("Would you like to play again? (yes/no)")
    while True:
        choice = input().lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print_slow("Invalid choice. Please enter 'yes' or 'no'.")


def main():
    while True:
        start_game()
        path = choose_path()
        result = explore_path(path)
        if result:
            print_slow("Congratulations! You won the game!")
        else:
            print_slow("Game Over!")
        if not play_again():
            print_slow("Thank you for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
