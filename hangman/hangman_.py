import random

# List of words for the game
words = ("apple", "orange", "banana", "coconuts", "pineapple")

# Art for hangman stages
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

# Function to display the current hangman state
def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

# Function to display the current hint (guessed letters)
def display_hint(hint):
    print(" ".join(hint))

# Function to display the correct answer when the game ends
def display_answer(answer):
    print("The correct word was:", answer)

# Main function for the Hangman game
def main():
    # Randomly select a word from the list
    answer = random.choice(words)
    hint = ["_"] * len(answer)  # Create a blank hint
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    print("Welcome to Hangman! Try to guess the word.")

    while is_running:
        # Display the current hangman state and hint
        display_man(wrong_guesses)
        display_hint(hint)
        
        # Get the player's guess
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        # Add the guess to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guess is in the answer
        if guess in answer:
            # Reveal the guessed letters in the hint
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            # Increment wrong guesses if the letter is not in the answer
            wrong_guesses += 1

        # Check win condition
        if "_" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            print("🎉 YOU WIN! Congratulations!")
            is_running = False

        # Check lose condition
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("😢 YOU LOSE! Better luck next time.")
            is_running = False

# Run the main game loop
if __name__ == "__main__":
    main()
