import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Du bist höher als der Computer. Verloren 😤"

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Sie haben verloren!"
    elif user_score == 0:
        return "Blackjack! Gewonnen!"
    elif user_score > 21:
        return "Du bist über 21, verloren!"
    elif computer_score > 21:
        return "Computer ist über 21, Gewonnen!"
    elif user_score > computer_score:
        return "Du hast gewonnen"
    else:
        return "Du hast verloren"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Deine Karten: {user_cards}, Aktueller Stand: {user_score}")
        print(f"Computer Erste Karte: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Möchten Sie noch eine Karte (j/n)\n")
            if user_should_deal == "j":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

        print(f"Dein letzter Zug war: {user_cards}, dein Endergebnis ist: {user_score}")
        print(f"Der letzte Zug des Computers war: {computer_cards}, das Endergebnis ist: {computer_score}")
        print(compare(user_score, computer_score))


while input("Möchtest du Blackjack spielen ? (j/n)") == "j":
    play_game()
