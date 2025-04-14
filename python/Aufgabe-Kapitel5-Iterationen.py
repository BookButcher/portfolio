# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:40:43 2025

@author: marcj
"""
# %% Kapitel 5 Notizen + Übungen
x = 0 
x = x + 1 #Inkrementieren
x = x - 1 #Dekrementieren

# While Schleife 
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')

# %% While Schleife mit break
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# %% While Schleife mit continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# %%For Schleife 
friends = ['Anna', 'Ben', 'Carla']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

# %%Zählen
count = 0
for itervar in [3, 41, 12, 9, 74, 15, 7, "f"]:
    count = count + 1
print('Count: ', count)

# %% Summieren
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
total = total + itervar
print('Summe: ', total)

# %% Maximum und Minimum ermitteln
largest = None

print('Maximum zu Beginn:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
        print('Betrachte Wert:', itervar, 'Aktuelles Maximum:', largest)
print('Das Maximum ist:', largest)


# %% Kapitel 5 Aufgabe 1
summieren = 0
counter = 0
durchschnitt = 0

while True:
    eingabe = input("Bitte eine Zahl eingeben: ")
    if eingabe == 'done':
        break
    
    try:
        eingabe = int(eingabe)
        summieren += eingabe
        counter += 1
        
        if counter > 0:
            durchschnitt = summieren / counter
        
    except:
        print("ungültige Eingabe")
  
print("Summe:", summieren)
print("Anzahl:", counter) 
print("Durchschnitt:", round(durchschnitt, 2))   

   

# %% Kapitel 5 Aufgabe 2

summieren = 0
counter = 0
lst = []
maximum = None
minimum = None


while True:
    eingabe = input("Bitte eine Zahl eingeben: ")
    if eingabe == 'done':
        break
    
    try:
        eingabe = int(eingabe)
        summieren += eingabe
        counter += 1
        
        lst.append(eingabe)
        
        
    except: 
        print("ungültige Eingabe")


for i in lst:
    if maximum is None or i > maximum:
        maximum = i

for i in lst:
    if minimum is None or i < minimum:
        minimum = i
        
print("Summe:", summieren)
print("Anzahl:", counter)
print("Das Maximum ist:", maximum)
print("Das Maximum ist:", minimum) 


        
        
        
        
        
        
