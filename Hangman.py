import random

# List of words with their hints
words_with_hints = {
    "python": "A popularg programming language",
    "apple": "A fruit that is often red or green",
    "guitar": "A string instrument",
    "hangman": "A word-guessing game",
    "pyramid": "A structure with a square base and triangular sides",
}

# Hangman stages visual representation
hangman_stages = [
    """
     ------
     |    |
     |    
     |   
     |    
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   
     |    
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |    |
     |    
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |    
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   /
     |
    ------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   / \\
     |
    ------
    """
]


# Function to get a random word and its hint
def get_random_word():
    word, hint = random.choice(list(words_with_hints.items()))
    return word, hint


# Function to display current progress
def display_progress(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)


# Main game function
def play_hangman():
    word, hint = get_random_word()
    guessed_letters = []
    attempts = 0
    max_attempts = len(hangman_stages) - 1

    print("Welcome to Hangman!")
    print(f"Hint: {hint}")

    while attempts < max_attempts:
        print(hangman_stages[attempts])
        print("Word progress:", display_progress(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print(f"Sorry, {guess} is not in the word.")
            attempts += 1
        else:
            print(f"Good guess! {guess} is in the word.")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print(hangman_stages[attempts])
        print(f"Game over! The word was: {word}")


# Start the game
play_hangman()
