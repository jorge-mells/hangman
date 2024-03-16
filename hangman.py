from dict import dictionary
import random
import re

def main():
    print(hangman())
 
def hangman():
    word = random.choice(dictionary)
    list = []
    for letter in word:
        if letter not in list:
            list.append(letter)
    lives = len(list)
    total = lives
    letters_used = []
    current_letters = ['-'] * len(word)
    while lives > 0:
        letters = ' '.join(letters_used)
        current = ' '.join(current_letters)
        print(f"You have {lives} lives left and have used these letters: {letters}")
        print(f"Current word: {current}")
        try:
            guess = input("\nGuess a letter: ")
            if not re.match(r"^[a-zA-Z]$", guess):
                raise ValueError
        except ValueError:
            continue
        if guess.lower() not in word:
            if guess.capitalize() in letters_used:
                print("\nYour letter has been already selected previously\n")
            else:
                lives -= 1
                letters_used.append(guess.capitalize())
                print(f"\nYour letter {guess.capitalize()} is not in the word\n")
        if guess.lower() in word:
            if guess.capitalize() in current_letters:
                print("\nYour letter is in the word\n")
            else:
                letters_used.append(guess.capitalize())
                print("\nYour letter has been added to the word\n")
            for i in range(len(word)):
                if guess.lower() == word[i]:
                    current_letters[i] = guess.capitalize()
        if ''.join(current_letters).lower() == word:
            print(f"Current word: {current}\n (test: {word})")
            return f"You have completed the game\nYour score: {lives}/{total}"
    return f"You have failed the game\nYour score: {lives}/{total}\nThe word was: {word}"
if __name__ == "__main__":
    main()