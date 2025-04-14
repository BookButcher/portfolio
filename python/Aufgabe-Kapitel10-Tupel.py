# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:37:31 2025

@author: marcj
"""

# %% Kapitel 10 Notizen + Übungen
# Tupel sind während der Laufzeit unveränderbar

# Tupel erstellen
t = (1, 2, 3, 4, 5)

# %% Tupel mit nur einem Wert
t1 = (1,)
print(t1)
print(type(t1))

# %% leeres tupel erstellen 
t = tuple()
print(t)

# %% Ergebnisse eines Tupels sind immer eine Sequenz
t = tuple('lupins')
print(t)

# %% Indexierung 
t = ('a', 'b', 'c', 'd', 'e')
print(t[0])
print(t[1:3])

# %% Ändern eines Tupels nicht möglich, aber ersetzen 
t = ('A',) + t[1:]
print(t)

# %% Vergleichen 
t1 = (1, 2, 4)
t2 = (0, 2, 3)

if t1 < t2:
    print(True)
else: 
    print(False)

# %% Sortieren
# Muster = DSU = Dekorieren, Sortieren, Extrahieren
# Liste von Wörtern nach Wortlängen absteigend sortieren:
    
txt = 'Es war die Nachtigall und nicht die Lerche'
# Text splitten 
words = txt.split()
# leere liste später tupel
t = list()

for word in words:
    # fügt die länge und das Wort in eine liste
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)

# %% Zuweisungs Magie
m = ['have', 'fun']
x, y = m

print(x, y)

# %% Tauschen von Zuweisungen
a = 1
b = 2
a, b = b, a

print(a)
print(b)

# %% ungeliche Menge von Werten zuweien
a, *b = (1, 2, 3, 4, 5) # Durch das Asterix wird alles nach 1 an b weitergegeben ((Un)Packing)
print(a)
print(b)

# %% Emailadresse in Benutzername und Domain teilen
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)

# %% Dictionary Methode "Items" 
# Gibt Liste von Tupeln zurück
# Jedes Tupel ist ein Schlüssel-Wert-Paar
d = {'b':1, 'a':13, 'c':7,}
t = list(d.items())
print(t) 

# Sortieren von Tupel zu Liste, Aufsteigend Alphabetisch
t.sort()
print(t)

# %% Mehrfachzuweisung mit Dictionarys
# Gibt ein Tupel in einer Liste wieder als neues Objekt "items"
d = {'b':1, 'a':13, 'c':7,}
for key, val in list(d.items()):
    print(val, key)

# %% Mit Werten statt der Schlüssel arbeiten
d = {'b':1, 'a':13, 'c':7,}
l = list()
for key, val in d.items():
    l.append((val, key))
print(l)  

# %% Sortieren der Liste nach Werten
l.sort()            # Vorwärts
print(l) 

l.sort(reverse=True) # Rückwerts
print(l)

# %% die 10 häufigsten Wörter heraus suchen 
import string

with open('romeo.txt', "r") as file:
    counts = dict()
    
    for line in file:
        line = line.translate(str.maketrans('', '', string.punctuation)) # Alles Sonderzeichen entfernen
        line = line.lower()                                              # Alle buchstaben klein
        words = line.split()                                             # Wörter einzeln Splite
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

# %% Sortieren des Wörterbuchs nach Wert
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)

# Tupel als Schlüssel in Dictionarys 
# Tupel können gehasht werden Listen nicht !

# Zusammengesetzten Schlüssel erstellen, geht nur mit Tupel
# Beispiel: Vorname, Nachname + Telefonnummer
last = 'Nöthen'
first = 'Marc'
number = '01764949484'
directory = dict()

directory[last, first] = number

for last, first in directory:
    print(first, last, directory[last, first])

# Zeichenketten, Listen und Tupel
# Wann bevorzugt man Tupel ?
# 1. bei return Anweisungen statt Listen besser Tupel 
# 2. Sequenz als Dictionaryschlüssel Tupel oder String
# 3. Sequenz als Argument an eine Funktion übergeben 
# Verringert unerwartetes Verhalten

# %% Kapitel 10 Aufgabe 1
# Das vorherige Programm soll auf folgende Weise überarbeitet werden:
# Die From-Zeilen sollen gelesen und geparst werden, um daraus die Adressen zu
# extrahieren. Dabei soll mit Hilfe eines Dictionarys die Anzahl der Nachrichten von
# jeder Person gezählt werden.
# Nachdem alle Daten gelesen wurden, soll die Person mit den meisten Nachrichten
# ausgegeben werden, indem eine Liste von (count, email)-Tupel aus dem Dictionary erstellt wird. Dann muss die Liste in umgekehrter Reihenfolge sortiert und
# schließlich die Person mit den meisten Nachrichten ausgegeben werden
# mbox-short.txt
filename = input('Enter the file name: ')


with open(filename, "r") as file:
    email_count = dict()
    unsorted_list = list()
    sorted_list = list()
    
    # Gehe alle zeilen in der Datei durch
    for line in file: 
        # speichere die zerlegten Wörter in variable words
        words = line.split()
        # Wenn From in der Variable Words vorkommt
        if 'From' in words:
            # Dann speichere das Wort anstelle 2 in Variable emailadress
            email_adress = words[1]
            # Zähle die Email adressen und Speichere sie in einem Dictionary mit Adresse und anzahl
            email_count[email_adress] = email_count.get(email_adress, 0) + 1
            
    # Durchlaufe Schlüssel und Wert aus Dictionary und speichere es in ein List Tupel Objekt       
    for key, val in list(email_count.items()):
        # Füge erst Wert dann Adress an das liste-Tupel Objekt an
        unsorted_list.append((val, key))
                
    #sorted_list.append(unsorted_list.sort(reverse=True))
    # Sortiere die Liste Absteigend 
    unsorted_list.sort(reverse=True)
    sorted_list = unsorted_list
    # Gib nur das erste List-Tupel Objekt aus 
    print(sorted_list[0])
    
    # Frage 1 Warum kann ich unsorted_list nicht in einer sorted_list speichern ?

# %% Kapitel 10 Aufgabe 2
# Schreiben Sie ein Programm, welches die Häufigkeit von Nachrichten
# pro Tageszeit (ganze Stunden) ermittelt. Die Stunden sollen aus der From-Zeile
# extrahiert werden, indem die Uhrzeit gefunden und diese Zeichenfolge dann anhand
# des Doppelpunkts in Teile zergliedert wird. Sobald die Nachrichtenhäufigkeit für
# jede Stunde gesammelt wurde, sollen diese wie weiter unten gezeigt ausgegeben
# werden (eine pro Zeile, sortiert nach Stunde)
# mbox-short.txt

filename = input('Enter the file name: ')

with open(filename, "r") as file:
    email_time_count = dict()
    unsorted_list = list()
    sorted_list = list()
    
    # Gehe alle zeilen in der Datei durch
    for line in file: 
        # speichere die zerlegten Wörter in variable words
        words = line.split()
        # Wenn From in der Variable Words vorkommt
        if 'From' in words:

            # Dann speichere das Wort anstelle 5 in Variable 
            time_list = words[5]
            # Zerlege Uhrzeit anstelle doppelpunkt
            time_list = time_list.split(':')
            # Speichere die Ganzen Stunden
            time_list = time_list[0]             
            # Zähle die Email adressen und Speichere sie in einem Dictionary mit Adresse und anzahl
            email_time_count[time_list] = email_time_count.get(time_list, 0) + 1          
            
    # Durchlaufe Schlüssel und Wert aus Dictionary und speichere es in ein List Tupel Objekt       
    for key, val in list(email_time_count.items()):
        # Füge erst Wert dann Adress an das liste-Tupel Objekt an
        unsorted_list.append((key, val))
        print(unsorted_list)         
    #sorted_list.append(unsorted_list.sort(reverse=True))
    # Sortiere die Liste Absteigend 
    unsorted_list.sort()
    sorted_list = unsorted_list
    # Gibt die Uhrzeit und die anzahl der emailadressen aus
    for time, count in sorted_list:
        print(time, count)       

# %% Kapitel 10 Aufgabe 3
# Übung 3: Schreiben Sie ein Programm, das eine Datei liest und die Buchstaben
# in absteigender Reihenfolge der Häufigkeit ausgibt. Das Programm sollte alle
# Eingaben in Kleinbuchstaben umwandeln und nur die Buchstaben a-z zählen. Es
# soll keine Leerzeichen, Ziffern, Interpunktionszeichen oder irgendetwas anderes als
# die Buchstaben a-z zählen. Dann sollen Textbeispiele in verschiedenen Sprachen
# als Eingabe dienen, um zu analysieren, wie die Buchstabenhäufigkeit zwischen
# verschiedenen Sprachen variiert. 
# Vergleichen Sie ihre Ergebnisse mit den Tabellen auf
# https://wikipedia.org/wiki/Letter_frequencies
# words.txt

# Eingabe Datei
filename = input('Gib einen Dateinamen an: ')

# Öffne Datei und Speichere Zeile für Zeile in File
with open(filename, 'r') as file:
    make_dict = {}
    make_list = []
    unsorted_list = []
    
    # gehe jedes Wort aus der zeile durch 
    for word in file:
        # Speichere die die Zeilen 
        words = word.lower().split()
        # Erstelle eine Tabelle in der die zu entfernenden Zeichen gespeichert sind
        table = str.maketrans('', '', string.punctuation)
        # Entferne alle zeichen aus tabelle 
        # Durchlaufe jedes zeile und speichere es in words ab 
        words = [word.translate(table) for word in words]
        
        # Durchlaufe jede zeile und speichere jedes wort
        for word in words:
            # nimm jedes Wort und speichere jeden Buchstaben
            for letter in word:
                # Speichere nur die Buchstaben A - Z 
                if letter not in ['ä', 'ö', 'ü', 'ß']:
                    # Zähle die Buchstaben und Speichere sie in einem Dictionary
                    make_dict[letter] = make_dict.get(letter, 0) + 1 
                    
    # Für den Schlüssel und den Wert            
    for key, val in make_dict.items():
        # Sortiere nach Wert und dann Schlüsse und füge sie einer Liste an
        unsorted_list.append((val, key))
        # Sortiere nach höchstem wert absteigend
        unsorted_list.sort(reverse=True)
    
    # Nimm jedes Schlüssel Wert paar
    for key, val in unsorted_list:
        # Gib Wert und dann Schlüssel aus 
        print(val, key)

# Verschiedene Sprachen als Txt
# words-short-de.txt
# words-short-en.txt
# words-short-franz.txt
# words-short-spanisch.txt
# words-short-arabisch.txt

