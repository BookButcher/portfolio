# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:36:18 2025

@author: marcj
"""

# %% Kapitel 8 Notizen + Übungen

# Zusammengesetzte Datentypen (listen, Dicts, Tupel)
# Listen
lst0 = []
lst1 = [10, 20, 30, 40]
lst2 = ['Banane', 'Apfel', 'Kiwi']
lst3 = ['spam', 2.0, 5, [10, 20]]
lst4 = [lst1, lst2, lst3]

# Listen sind veränderbar, Zeichenketten nicht
# Zugriff auf Elemente über index
print(lst1[0])

# %% Zuweisen Element
numbers = lst1 # Kopie der Liste
numbers[0] = 100
print(numbers)

# In operator funktioniert
# %% For Schleife 
for number in numbers:
    print(number)

# %% schreiben oder aktualisieren 
for i in range(len(numbers)):
    numbers[i] = numbers[i] + 1 # alle werte um 1 erhöhen
    
print(numbers)

# %% Listen Operationen 
# Subtraktion und Division geht nicht 
a = [1, 2, 3]
b = [4, 5, 6]

# %% Verketten
c = a + b
print(c)

# %% Listen multiply
d = [1] * 4
print(d)

# %% Slicing
a = ['a', 'b', 'c', 'd', 'e']
print(a[1:2])

# %% Zuweisung durch Slicing
a = ['a', 'b', 'c', 'd', 'e']
a[1:3] = [1, 2]
print(a)

# %% Methoden 
# anfügen einzel Element
a = ['a', 'b', 'c', 'd', 'e']
a.append(1)
print(a)

# %% Mehrere Elemente anfügen 
a = ['a', 'b', 'c', 'd', 'e']
b = ['z', 'y']
a.extend(b)
print(a)

# %% Sortieren 
a.sort()
print(a)

# %% mit kopie
a = ['a', 'b','e', 'c', 'd']
b = sorted(a)
print(b)

# %% löschen und extrahieren 
a = ['a', 'b','e', 'c', 'd']
b = a.pop(2)
print(a)
print(b)

if b == 'e':
    print("Extracted")
# %% del -> löscht wie pop aber element ist weg
# remove löscht element ohne index zu kennen bsp
a = ['a', 'b', 'a']
a.remove('a')
print(a)

# %% Mehrere löschen mit slicing (exclusive 5)
a = ['a', 'b','e', 'c', 'd','e']
del a[1:5]
print(a)

# %% Funktionen
# len, max, min, sum(geht nur mit nummern)

numlist = list()
while (True):
    inp = input('Gib eine Zal ein: ')
    
    if inp == 'done': break

    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Mittelwert:', average)


# %% Konvertieren von string in liste
s = 'spam'
t = list(s)
print(t)

# %% Wort liste in einzelne Wörter splitten
s = 'pining for the fjords'
t = s.split()
print(t)
print(t[2])

# %% trennen an spezifischem Zeichen 
s = 'rama-lama-ding-dong'
delimiter = '-'
x = s.split(delimiter)
print(x)

# %% wieder zusammen fügen
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
x = delimiter.join(t)
print(x)
print(type(x)) # -> String

# %% Datei Parsen 
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words)
    print(words[2])

# %% Prüfen auf selbes Objekt
a = 'Apfel'
b = 'Apfel'
c = a is b
print(c)

# %% Löscht bestimmte elemente aus einer Liste 
def bad_delete_head(t):
    return t[0:2]


t = [1, 2, 3, 4]
y = bad_delete_head(t)
print(y)
print(t)

# %% Listen Tests append und + unterschiede 
t = [1, 2, 3, 4, 5, 6]
x = [7, 8, 9]

t.append([x])
print(t)
t = t.append(x)

print(t + [x])

y = t + x

print(y)
print(t)

# %% Original und Kopie, Original behalten Kopie sortieren
t = [1, 4, 2, 5, 3, 8, 4, 5, 6]
orig = t[:]
print(orig)
t.sort()
print(t)


# %% Prüft beim Parsen der Datei auf Leerzeilen (Debug modus)
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0: continue
    if words[0] != 'From': continue
    print(words[2])

# Leitsatz, was könnte schief gehen ?? 

# %% Kapitel 8 Aufgabe 1

# Löscht den Angegebenen Wert einer Liste
def remove_all(lt, value): 
    while value in lt:
        lt.remove(value)
    
    
number = ['1', '2', '3', '2', '4', '5', '2', '2',]
remove_all(number, '2')    
print(number)


# %% Kapitel 8 Aufgabe 2

def chop(lte):
    del lte[0]
    del lte[-1]
    return None

x = [1, 2, 3, 4, 5, 6]
chop(x)
print(x)

def middle(lte2):
    return lte2[1:-1]

z = [1, 2, 3, 4, 5, 6]
w = middle(z)
print(w)

# Genaue überprüfung ob ein Objekt sich geändert hat
print(id(w))
print(id(z))

# %% Kapitel" 8 Aufgabe 3

try:
    #fhand = open('mbox-short.txt')
    fhand = open('debug_datei.txt') # -> Test Datei
    for line in fhand:
        words = line.split()
        print('Debug:', words)
        if len(words) == 0: continue
        if words[0] != 'From': continue
        if len(words) < 3 or len(words) > 4: continue # -> Bugs gedunden 
        print(words[2])

except FileNotFoundError: # -> Try & Except eingebaut !
    print("Fehler: Datei nicht gefunden!")
    exit()


# %% Kapitel 8 Aufgabe 4

fhand = open('mbox-short.txt')

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From': 
        continue
    print(words[:])


# %% Kapitel 8 Aufgabe 5

# Alle einzigartigen Wörter in einer Datei finden
wortliste = ['soft','yonder', 'window', 'breaks','east', 'Juliet','sun',
             'Arise', 'fair', 'sun', 'kill', 'envious', 'moon',
             'already', 'sick', 'pale', 'grief']

einzigartige_wortliste = []

fromeo = open('romeo.txt')
for line in fromeo:
    words = line.split()
    print(words)
    for word in words:
        if word not in wortliste and word not in einzigartige_wortliste:
            einzigartige_wortliste.append(word.lower())
            einzigartige_wortliste.sort()
        else:
            continue
        
print('--------------------------------------------------')       
# new_list = list(set(einzigartige_wortliste))
print(einzigartige_wortliste)

# %% Kapitel 8 Aufgabe 6
counter = 0

try:
    fhand = open('mbox-short.txt')
    for line in fhand:
        
        words = line.split()
        if 'From' in words:
            counter = counter + 1
            name = words[1]
            print(name)
            
    print("Es gibt", counter, "Zeilen mit 'From' als erstem Wort " )
            
except FileNotFoundError: # -> Try & Except eingebaut !
    print("Fehler: Datei nicht gefunden!")
    exit()


# %% Kapitel 8 Aufgabe 7

user = None
convert_benutzer = []
aktuelle_nummer = 0
maximum = 0
minimum = 0

while user != 'done':
    user = input("Bitte Zahlen eingeben: (wenn fertig, mit done Beenden)\n")
    if user == 'done':
        break
    convert_benutzer.append(int(user))
    print(convert_benutzer)
    

kleinste_zahl = convert_benutzer[0]

for number in convert_benutzer:
    aktuelle_nummer = number
    
    if aktuelle_nummer > maximum:
        maximum = aktuelle_nummer
    
    if aktuelle_nummer < kleinste_zahl:
        kleinste_zahl = aktuelle_nummer
        minimum = aktuelle_nummer   
    

print("Minimum:", minimum)
print("Maximum: ", maximum)







