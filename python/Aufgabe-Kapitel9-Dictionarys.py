# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:37:06 2025

@author: marcj
"""
# %% Kapitel 9 Notizen + Übungen
# Datensäätze schnell wiederfinden ist ausschlaggebend für Dictionarys
# Schlüssel(Key) + Wert(Value)

# Beispiel - Englisch / Deutsch - Wörterbuch
# Leeres Dictionary 
eng2de = dict()
print(eng2de)

# %% Elemente hinzufügen / one = Schlüssel, eins = Wert
eng2de['one'] = 'eins'
print(eng2de)

# %% Weiter Methoden zum hinzufügen von Elementen 
eng2de = {'one': 'eins', 'two': 'zwei', 'three': 'drei'}
print(eng2de)

# %% Indizieren anhand von Schlüssel
print(eng2de['two'])

# %% Länge eines Dictionarys, zählt die Paare als 1
print(len(eng2de))

# In-Operator, Boolesche Werte als Rückgabe, Sucht nur nach Schlüssel 
print('one' in eng2de)
print('eins' in eng2de)

# %% Mit Methode values nach Werten suchen
vals = list(eng2de.values())
print('eins' in vals)

# In Operator bei Listen = Linearer Suchalgorithmus
# In Operator bei Dictionarys = Hash Algorithmus (schneller)

# Dictionary zum Zählen verwenden 
# Beispiel Zeichenkette 
# Wie oft kommt jeder Buchstabe vor ? 

# 1. Möglichkeit
# 26 Variablen erstellen, Wortdurchlaufen und entsprechenden Buchstaben inkrementieren

# 2. Möglichkeit 
def count_characters(text):
    # Eine Liste mit 26 Nullen erstellen (für jeden Buchstaben im Alphabet)
    counter = [0] * 26
    
    # Text in Kleinbuchstaben umwandeln, um Groß- und Kleinschreibung zu ignorieren
    text = text.lower()
    
    # Durch jeden Buchstaben im Text iterieren
    for char in text:
        # Prüfen, ob der Charakter ein Buchstabe ist
        if 'a' <= char <= 'z':
            # ord('a') = 97, also ziehen wir 97 ab, um Indizes von 0-25 zu erhalten
            index = ord(char) - ord('a')
            counter[index] += 1
    
    # Ergebnisse ausgeben
    for i in range(26):
        # char entspricht dem Buchstaben bei Index i
        char = chr(i + ord('a'))
        print(f"'{char}': {counter[i]}")
    
    return counter

# Beispiel
text = "Hello, World!"
count_characters(text)


# %% 3. Möglichkeit
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

# %% get Methode, nimmt einen schlüssel und standardwert an
# Behandelt den Fall dass ein Schlüssel nicht in einem Dictionary enthalten ist
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)

# %% Dictionarys und Dateien
# Die Kombination der beiden verschachtelten Schleifen stellt sicher, 
# dass wir jedes Wort in jeder Zeile der Eingabedatei zählen
filename = input('Enter the file name: ')
try:
    with open(filename, "r") as file:
        counts = dict()
        for line in file:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1 # ist das selbe wie eine zeile drunter, aber schneller
                # if word not in counts: 
                #     counts[word] = 1
                # else:
                #     counts[word] += 1
                if counts[word] > 1:                   # Gibt alle Schlüssel und Werte aus die über 1 liegen
                    print(word, counts[word])
        print(counts)
except:
    print('File cannot be opened:', filename)
    exit()

# %% Schleifen und Dictionarys
# key = Schlüssel ausgabe, counts[key] = Wert ausgabe
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    print(key, counts[key]) 

# %% Alle Werte über ....
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    if counts[key] > 1:
        print(key, counts[key]) 

# %% Alphabetische Reihenfolge, Liste erstellen aus Dict
counts = { 'chuck': 1 , 'annie': 42, 'jan': 100}
lst = list(counts.keys())
print(lst)
lst.sort() # sortiert Alphabetisch
for key in lst:
    print(key, counts[key]) 
    
# %% Fortgeschrittene Textanalyse
# Sonderzeichen Zeichen finden und Groß-Kleinschreibung 

# *String Methoden* 
import string
# lower         -> alle buchstaben klein
# punctuation() -> Sonderzeichen ermitteln
# translate()   -> kann auf die Ersetzungstabelle angewendetet werden
# maketrans()   -> Erstellt eine Ersetzungstabelle, alle zeichen die ersetzt oder gelöscht werden 

table = str.maketrans('', '', string.punctuation)
print(table)
# Erstes Argument ('') → Keine Zeichen werden ersetzt.
# Zweites Argument ('') → Keine Zeichen werden ersetzt.
# Drittes Argument (string.punctuation) → Diese Zeichen werden entfernt.

line = line.translate(table)
# Jedes Satzzeichen aus string.punctuation wird gelöscht.
# Alle anderen Zeichen bleiben unverändert.

text = "Hello, world! How's it going?"
table = str.maketrans('', '', string.punctuation)
clean_text = text.translate(table)

print(clean_text)  
 
'------------------------------------------------------'

# %% Alle Sonderzeichen entfernen
filename = input('Enter the file name: ')

try:
    with open(filename, "r") as file:
        counts = dict()
        for line in file:
            # entfernt alle nachgestellten Leerzeichen und bestimmte Zeichen am Ende eines Strings
            line = line.rstrip() 
            # translate übersetzt die tabelle, maketrans erstellt die Tabelle 
            line = line.translate( 
                       line.maketrans('', '', string.punctuation)) # alle Satzzeichen 3 Argumente 
            # alle buchstaben klein
            line = line.lower()
            # Spliten der Wörter
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1
        print(counts)
        
except:
    print('File cannot be opened:', filename)
    exit()

# %% Kapitel 9 Aufgabe 1
# mbox-short.txt
# Leeres Dictionary
word_dict = dict()

# Benutzer kann eine Datei eingeben
filename = input("Gib eine Datei an: ")
# Öffne Datei mit Readmodus
with open(filename, "r") as file:
    # loop durch jede zeile
    for line in file:
        # splite jedes word am leerzeichen 
        words = line.split()
        # loop für jedes Word
        for word in words:
            # Speichere jedes Wort als Schlüssel und jeden Wert als ersten Buchstaben
            word_dict[word] = word[0]
            
print(word_dict)
print('stumpfsinnig' in word_dict)

# %% Kapitel 9 Aufgabe 2
# Schreiben Sie ein Programm, das jede E-Mail-Nachricht danach kategorisiert, 
# an welchem Wochentag sie versendet wurde. Suchen Sie dazu nach Zeilen,
# die mit „From“ beginnen, suchen Sie dann nach dem dritten Wort und führen Sie
# eine laufende Zählung der einzelnen Wochentage durch. Am Ende des Programms
# geben Sie den Inhalt Ihres Dictionarys aus (die Reihenfolge spielt keine Rolle)
#    mbox-short.txt

filename = input('Enter the file name: ')

try:
    with open(filename, "r") as file:
        counts = dict()
        
        for line in file:
            words = line.split()
            
            if 'From' in words:
                words = words[2]
                # print(words)
                counts[words] = counts.get(words, 0) + 1 
                
                # if words not in week_days:
                #     week_days[words] = 1
                # else:
                #     week_days[words] += 1
                
    print(counts)      
                
except:
    print('File cannot be opened:', filename)
    # exit()

# %% Kapitel 9 Aufgabe 3
# Schreiben Sie ein Programm, um ein E-Mail-Protokoll zu lesen. Erzeugen
# Sie ein Histogramm mithilfe eines Dictionarys, um zu zählen, wie viele Nachrichten
# von den einzelnen E-Mail-Adressen gekommen sind. Geben Sie das Dictionary dann aus.
#    mbox-short.txt

filename = input('Enter the file name: ')
try:
    with open(filename, "r") as file:
        counts = dict()
        for line in file:
            words = line.split()
            if 'From' in words:
                word = words[1]
                counts[word] = counts.get(word, 0) + 1
                if counts[word] > 2:                  
                    print(word, counts[word])
        # print(counts)
except:
    print('File cannot be opened:', filename)
    # exit()

# %% Kapitel 9 Aufgabe 4
# Fügen Sie folgendes dem obigen Programmcode hinzu, um herauszufinden,
# wer die meisten Nachrichten in der Datei erhalten hat. Nachdem alle Daten
# gelesen und das Dictionary erstellt wurde, durchsuchen Sie das Dictionary mithilfe
# einer Schleife nach dem Maximum (siehe Kapitel 5: Maximum und Minimum ermitteln), 
# um herauszufinden, wer die meisten Nachrichten hat, und geben Sie aus,
# wie viele Nachrichten die Person bekommen hat.
# mbox-short.txt

filename = input('Enter the file name: ')

try:
    with open(filename, "r") as file:
        count_emails = dict()
        make_list = []
        for line in file:
            words = line.split()
            if 'From' in words:
                email_adress = words[1]
                
                count_emails[email_adress] = count_emails.get(email_adress, 0) + 1
                
                take_numbers = count_emails[email_adress]
                make_list.append(take_numbers)
                # if counts[word] > 2:                  
                    # print(word, counts_the_emails[word])
                
        most_emails = None
        for find_max in make_list:
            if most_emails is None or find_max > most_emails:
                most_emails = find_max
        print('Die meisten Emails hat: ', email_adress, "mit", most_emails, "Nachrichten")
            
except:
    print('File cannot be opened:', filename)
    # exit()

# %% Kapitel 9 Aufgabe 5
# Dieses Programm zeichnet nur den Domänennamen (anstelle der Adresse)
# auf, von dem die Nachricht gesendet wurde, also nicht, von welchem konkreten
# Absender die E-Mail kam (das wäre die gesamte E-Mail-Adresse). Geben Sie am
# Ende des Programms den Inhalt Ihres Dictionarys aus.
# mbox-short.txt

filename = input('Enter the file name: ')
count_emails = dict()

try:
    with open(filename, "r") as file:
        count_emails = dict()
        
        for line in file:
            words = line.split()
            if 'From' in words:
                email_adress = words[1]
                domain = email_adress.split('@')[1]
                count_emails[domain] = count_emails.get(domain, 0) + 1
                
        print(count_emails)

except:
    print('File cannot be opened:', filename)
    # exit()

# %% Test Center
