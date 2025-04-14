# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:41:11 2025

@author: marcj
"""
# =============================================================================
# Notizen aus Kapitel 3 
# =============================================================================
# Bool ist kein Datentyp sondern eine Klasse vom Typ bool
# Vergleichs Operatoren:
    
#   x != y        # x ist ungleich y
#   x > y         # x ist groesser als y
#   x < y         # x ist kleiner als y
#   x >= y        # x ist groesser oder gleich y
#   x <= y        # x ist kleiner oder gleich y
#   x is y        # x bezeichnet das selbe Objekt wie y
#   x is not y    # x bezeichnet nicht das selbe Objekt wie y

# Logische Operatoren:
    
# and             # x > 0 and x < 10
# or              # n%2 == 0 or n%3 == 0
# not             # not (x > y) -> Nur wahr wenn x kleiner y

# Tipp: 17 and True ist immer True -> kann nützlich sein 

# Bei Zusammengesetzen Anweisungen muss immer mindestens 1 Anweisung im Rumpf 
# stehen, als Platzhalter kann man "pass" nutzen 

# %% Kapitel 3 Aufgabe 1
# Lösung 1
eingabeabs = input("Wie viele Stunden hast du gearbeitet: ") 
arbeitsstunden = float(eingabeabs)
stundenlohn = 10
mtlgehalt = stundenlohn * arbeitsstunden

if(arbeitsstunden > 40):
    
    mtlgehalt = mtlgehalt + ((stundenlohn * 1.5) - stundenlohn) * (arbeitsstunden - 40)

print(mtlgehalt)

# %% Lösung 2
eingabeabs = input("Wie viele Stunden hast du gearbeitet: ") 
arbeitsstunden = float(eingabeabs)
stundenlohn = 10

if(arbeitsstunden > 40):
    nst = 40
    gstabs = arbeitsstunden - nst
    asg = gstabs * 1.5 * 10
    gesamt = asg + (nst * 10) 
    print(gesamt)
else:
    gesamtnl = arbeitsstunden * 10
    print(gesamtnl)

# %% Kapitel 3 Aufgabe 2

try:
    eingabeabs = input("Wie viele Stunden hast du gearbeitet: ")
    arbeitsstunden = float(eingabeabs)
    eingabestdl = input("Eingabe Stundenlohn: ")
    stundenlohn = float(eingabestdl)
    mtlgehalt = stundenlohn * arbeitsstunden

    if(arbeitsstunden > 40):
        
        mtlgehalt = mtlgehalt + ((stundenlohn * 1.5) - stundenlohn) * (arbeitsstunden - 40)

    print(mtlgehalt)
except:
    print("Bitte geben Sie nur Dezimalzahlen ein!")

# %% Kapitel 3 Aufgabe 3
eingabenote = input("Bitte gib eine Dezimalzahl zwischen 0,0 und 1,0 an: ")
eingabenote = float(eingabenote)


if eingabenote > 1.0:
    print("Fehler, nur Zahlen zwischen 0.0 und 1.0")
elif eingabenote >= 0.9:
    print("Note: 1")
elif eingabenote >= 0.8:
    print("Note: 2")
elif eingabenote >= 0.7:
    print("Note: 3")
elif eingabenote >= 0.6:
    print("Note: 4")
elif eingabenote < 0.6 and eingabenote >= 0.0:
    print("Note: 5")
    

