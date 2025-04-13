import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)

display = []

for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Bitte geben Sie ein Buchstaben ein: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess in display:
        print(f"You've already guessed {guess}")
        print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, "
              f"that's not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You win !")

    print(stages[lives])