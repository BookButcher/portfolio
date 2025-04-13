# Hangman
import random
from repeating_art import *
from repeating_word import *

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(f"Logo{logo}")

display = []
for _ in range(word_length):
    display += '_'

while not end_of_game:
    guess = input("Please Enter a letter: ").lower()

    if guess in display:
        print(f"You´re letter is {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"The chosen letter {guess} is not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])
