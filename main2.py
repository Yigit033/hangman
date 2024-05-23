### More Professional Code Version of Hangman Game ###

import random

word_categories = {
    'chicken': 'Animals',
    'cloud': 'Nature',
    'python': 'Programming',
    'computer': 'Technology',
    'book': 'Culture'
}

def select_word():
    word = random.choice(list(word_categories.keys()))
    category = word_categories[word]
    return word, category

def initialize_hidden_word(word):
    """Initializes the hidden word with '_' characters."""
    return ['_' for _ in word]

def play_hangman():
    """Plays the hangman game."""
    word, category = select_word()
    hidden_word = initialize_hidden_word(word)
    guess_count = 0
    max_guess = 5

    print("Welcome to Hangman Game!")
    print(f"Category: {category}")

    while '_' in hidden_word and guess_count < max_guess:
        print("Hidden Word:", ' '.join(hidden_word))
        guess = input("Guess a letter: ").lower()

        if guess in hidden_word:
            print("You have already guessed this letter.")
            continue

        guess_count += 1
        found = False

        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = letter
                guess_count -= 1
                found = True

        if found:
            print("Correct guess!")
        else:
            print(f"Wrong guess! Number of guessing remaining : {max_guess - guess_count}")
            
        
    if '_' not in hidden_word:
        print(f"Congratulations, you guessed the word! Word: {word}")
    else:
        print("Sorry, you couldn't guess the word. You ran out of guesses. Correct word:", word)

if __name__ == "__main__":
    play_hangman()
