"""
###### Pseudo Code #######
1.  Überschrift der gesuchten Anfrage
2.  Die Anfrage in Zahlen
3.  Text "durschnittle monatliche Suchanfragen
4.  Es werden zwei Anfragen angezeigt die Obere Zeigt das Volle Ergebnis
5.  Die Untere zeigt nur die Überschrift und man kann zwischen höher und Drunter wählen
6.  Es wird immer das vorige mit einem Zufälligen Verglichen
7.  liegt man falsch, ist das Spiel vorbei
8.  Es wird immer die Aktuelle Punktezahl angezeigt
9.  Am Ende wird nochmal ide Punkte Zahl ausgegeben und ein Text dazu
"""

import random
from game_data import data
from art import logo, vs

print(logo)

total = 0
again = True

while again != False:
    """ #Lösung des Coach
    account_a = random.choice(data)
    account_b = random.choice(data)
    
    account_name = account_a["name"]
    account_descr = account_a["description"]
    account_country = account_a["country"]
   
    """
    # Zufälliges Dictionarys für den Vergleich
    compare_a = random.randrange(len(data))
    compare_b = random.randrange(len(data))

    # Name, Beschreibung & Land für die Text Verarbeitung aus Dict aus compare a
    compare_a_name = data[compare_a]['name']
    compare_a_beschreibung = data[compare_a]['description']
    compare_a_land = data[compare_a]['country']
    compare_a_follower = data[compare_a]['follower_count']

    # Name, Beschreibung & Land für die Text Verarbeitung aus Dict aus compare a
    compare_b_name = data[compare_b]['name']
    compare_b_beschreibung = data[compare_b]['description']
    compare_b_land = data[compare_b]['country']
    compare_b_follower = data[compare_b]['follower_count']

    print(f"Compare A: {compare_a_name}, {compare_a_beschreibung}, {compare_a_land}")

    print(vs)

    print(f"Compare B: {compare_b_name}, {compare_b_beschreibung}, {compare_b_land}")

    user_choice = input("Who has more followers? Type 'A' or 'B'\n")
    if user_choice == 'A':
        if compare_a_follower > compare_b_follower:
            total += 1
            print(f"A was right You´re Score: {total}")
        elif compare_a_follower < compare_b_follower:
            print(f"Sorry, that's wrong. Final Score {total}")
            again = False
    elif user_choice == 'B':
        if compare_b_follower > compare_a_follower:
            total += 1
            print(f"B was right You´re Score: {total}")
        elif compare_b_follower < compare_a_follower:
            print(f"Sorry, that's wrong. Final Score {total}")
            again = False






