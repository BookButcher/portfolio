
# Blackjack Project

# Difficulty Normal 😎: Use all Hints below to complete the project.
"""
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

## Die Größe des Decks ist unbegrenzt.
## Es gibt keine Joker.
## Bube/Dame/König zählen alle als 10.
## Das Ass kann als 11 oder 1 zählen.
## Verwenden Sie die folgende Liste als Kartenspiel:
## Karten = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## Die Karten in der Liste haben die gleiche Wahrscheinlichkeit, gezogen zu werden.
## Die Karten werden nicht vom Stapel entfernt, wenn sie gezogen werden.
## Der Computer ist der Geber.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
# Tipp 1: Gehen Sie auf diese Website und probieren Sie das Blackjack-Spiel aus:
#   https://games.washingtonpost.com/games/blackjack/

# Then try out the completed Blackjack project here:
# Probieren Sie dann das fertige Blackjack-Projekt hier aus:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
# Tipp 2: Lesen Sie diese Aufschlüsselung der Programmanforderungen:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.
# Versuchen Sie dann, Ihr eigenes Flussdiagramm für das Programm zu erstellen.

# Hint 3: Download and read this flow chart I've created:
# Tipp 3: Laden Sie dieses von mir erstellte Flussdiagramm herunter und lesen Sie es:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# Tipp 4: Erstellen Sie eine deal_card()-Funktion, die mit Hilfe der unten stehenden Liste eine zufällige Karte *zurückgibt*.
# 11 is the Ace.
# Nr. 11 ist das Ass.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# Tipp 5: Geben Sie dem Benutzer und dem Computer jeweils 2 Karten mit deal_card() und append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# Tipp 6: Erstellen Sie eine Funktion namens calculate_score(), die eine Liste von Karten als Eingabe nimmt
# and returns the score.
# und den Punktestand zurückgibt.
# Look up the sum() function to help you do this.
# Schauen Sie sich die Funktion sum() an, um dies zu tun.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
# Tipp 7: Prüfen Sie in calculate_score(), ob ein Blackjack vorliegt (ein Blatt mit nur 2 Karten: Ass + 10) und geben Sie 0 anstelle des tatsächlichen Ergebnisses zurück.
0 wird in unserem Spiel einen Blackjack darstellen.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
# Tipp 8: Prüfen Sie innerhalb von calculate_score() auf eine 11 (Ass). Wenn die Punktzahl bereits über 21 liegt, entfernen Sie die 11 und ersetzen Sie sie durch eine
1. Vielleicht müssen Sie append() und remove() nachschlagen.

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
# Tipp 9: Rufen Sie calculate_score() auf. Wenn der Computer oder der Benutzer einen Blackjack (0) hat oder wenn der Punktestand des Benutzers über 21 liegt, dann endet das Spiel.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List.
If no, then the game has ended.
# Tipp 10: Wenn das Spiel noch nicht beendet ist, fragen Sie den Benutzer, ob er eine weitere Karte ziehen möchte. Wenn ja, dann benutzen Sie die Funktion deal_card(),
um eine weitere Karte zur Liste user_cards hinzuzufügen. Wenn nein, dann ist das Spiel beendet.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
# Hinweis 11: Der Punktestand muss bei jeder neu gezogenen Karte überprüft werden, und die Überprüfungen in Hinweis 9 müssen bis zum Ende des Spiels wiederholt werden.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
# Tipp 12: Sobald der Benutzer fertig ist, ist es an der Zeit, den Computer spielen zu lassen. Der Computer sollte so lange Karten nachziehen, wie er weniger als 17 Punkte hat.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw.
If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses.
If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
# Tipp 13: Erstellen Sie eine Funktion namens compare() und übergeben Sie user_score und computer_score. Wenn der Computer und der Benutzer die gleiche Punktzahl haben,
dann ist es ein Unentschieden. Wenn der Computer einen Blackjack (0) hat, dann verliert der Benutzer. Wenn der Benutzer einen Blackjack (0) hat, dann gewinnt der Benutzer.
Wenn der user_score über 21 liegt, verliert der Benutzer. Wenn der computer_score über 21 liegt, verliert der Computer. Wenn keine der oben genannten Bedingungen zutrifft,
gewinnt der Spieler mit der höchsten Punktzahl.


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
# Tipp 14: Fragen Sie den Benutzer, ob er das Spiel neu starten möchte. Wenn er dies bejaht, löschen Sie die Konsole und starten Sie eine neue Partie Blackjack
und zeigen Sie das Logo aus art.py.
"""