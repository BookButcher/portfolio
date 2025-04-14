# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:03:14 2025

@author: marcj
"""
# =============================================================================
# Dokumentation Kapitel 2 Bezeichner, Ausdrücke und Anweisungen
# =============================================================================

# =============================================================================
# Alles, was man zu einem Wert auswerten kann ist ein Ausdruck 
# Fest angegebene Werte sind sogenannte Konstanten, aber auch komplexere 
# Ausdrücke, bei denen mehrere Teile durch Operatoren verknüpft sind. 
# Mit einer Zuweisung einzelner Werte kann man über Ihren Bezeichner verwenden

# Alle Daten sind als Objekte abgespeichert, Funktionen sind Objekte und 
# Objekte sind Objekte ! Alles in Python ist ein Objekt

# Anweisungen sind eine Einheit von Code
# Ein Ausdruck ist eine Kombination aus Werten, Variablen und Operatoren, die
# wiederum zu einem Wert abgeleitet werden kann

# Reihenfolge der Auswertung: 
# Mathematische Reihenfolge auch in Python
# Klammern -> Potenzrechnung -> Multi und Divi -> Add und subtract 
# Potenz ** wird von rechts nach links ausgewertet

# Objekte haben Datentypen("Int", "Float", "String")
# =============================================================================

# %% Kapitel 2 Aufgabe 2
name = input("Wie lautet dein Name: ")
print("Hallo " + name)

# %% Kapitel 2 Aufgabe 3

eingabeabs = input("Wie viele Stunden hast du gearbeitet: ") 
arbeitsstunden = float(eingabeabs)
stundensatz = 2.75

berechnung = float(arbeitsstunden * stundensatz)
print(berechnung)

# %% Kapitel 2 Aufgabe 4

breite = 17
hoehe = 12.0

a = breite // 2
print(type(a))
b = breite / 2.0
print(type(b))
c = hoehe / 3
print(type(c))
d = 1 + 2 * 5 
print(type(d))

# %% Kapitel 2 Aufgabe 5


temp = input("Gib die Temperatur in Celsius ein: ")
tempcast = float(temp)

fahrenheit = tempcast * 1.8 + 32
print(fahrenheit)


