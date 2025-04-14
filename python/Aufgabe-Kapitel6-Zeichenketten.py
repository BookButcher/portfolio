# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:59:16 2025

@author: marcj
"""


# %% Kapitel 6 Notizen + Übungen

frucht = 'Apfel'
zahlen = [1, 2, 3, 4]
zahl = '523'
convert = zahl[1]
convert = int(convert)
print("Liste: ",zahlen[0])
print("Zahl indexieren: ",convert)
print("Bustabenstelle: ",frucht[3])
print("Länge des Wortes: ",len(frucht))

# %% letztes Zeichen 
last = len(frucht)
print("Letzteszeichen: ",frucht[last-1])

# %% mittleres Zeichen
mid = len(frucht)
print("Aktuelle Länge des Wortes: ",mid)
if mid % 2 != 0: # Rest ungleich 0 dann 
    mid = int(mid / 2) + 1 # addiere + 1, aufrunden
print("Mittelwert: ",mid)
print("Ausgabe Buchstabe: ",frucht[mid])

testzeichen = 'Hallo Welt wie geht es dir ?'
count_l = 0
count_t = 0

# %% Auf Leerzeichen in Zeichenkette prüfen 
for i in testzeichen:
    if i == ' ':
        count_l +=1
    elif i == 't':
        count_t += 1
print("Satz: ", testzeichen)
print("Leerzeichen: ",count_l)
print("Buchstaben mit 't': ",count_t)

# %% Iteriere über jeden Buchstaben und gib aus. 
index = 0
while index < len(frucht):
    zeichen = frucht[index]
    print(zeichen)
    index = index + 1

# %% Slicing 
txt = 'Monty Python'
txt1 = txt[0:5]
txt2 = txt[6:12]
print(txt1)
print(txt2)

# %% Variable halten, erstes Wort. 
print(txt)

lst = []
for i in txt:
    lst += i
    if ' ' in lst:
        lst.pop()
        break
        
new_string = ""
new_string = new_string.join(lst) 
print(new_string)

# in operator gibt True zurück wenn gesuchtes vorhanden 
# stuff = 'Hello world'
# type(stuff) -> zeigt die type eines Objekts an 
# dir(stuff) -> zeigt die Methoden eines Objekts an 
# help(str) -> vollständige Hilfe 

# %% Wichtige Methoden
word = " Hello Armina "
x = word.find('lo')
print(x)

y = word.strip()
print(y)

# %%Finde teilsätze

txt = 'Hätte ich ein @wäredasganznett !'
find1 = txt.find('@')
print(find1)

find2 = txt.find(' ', find1)
print(find2)

gesamt_find = txt[find1+1:find2]
print(gesamt_find)


# %% F-Strings
count = 2
zeichen = 'a'
print(f'Buchstabe: {zeichen} Anzahl: {count}')

# %% oder 
anteil = 10/3
print(f"Ihr Anteil ist {anteil:.2f}")

# %% Kapitel 6 Aufgabe 1

index = len(frucht) - 1 

while index >= 0:
    zeichen = frucht[index]
    print(zeichen)
    index = index - 1
    

# %% Mit For Schleife 
index = len(frucht) - 1 

for i in frucht:
    zeichen = frucht[index]
    print(zeichen)
    index = index - 1


# %% Kapitel 6 Aufgabe 2

frucht = 'Apfel'
print(frucht[:])

print(frucht[0:0])
print(frucht[0:1])
print(frucht[0:-1])



# %% Kapitel 6 Aufgabe 3

word = 'Banane'
count = 0
for zeichen in word:
    if zeichen == 'a':
        count = count + 1
print(count)


def count(word):
    counter = 0
    for zeichen in word:
        if zeichen == 'a':
            counter += 1
    return counter

print(count('Banane'))



# %% Kapitel 6 Aufgabe 4

txt = 'Banane'
x = txt.count('a')
print(x)


# %% Kapitel 6 Aufgabe 5

strings = 'X-DSPAM-Confidence: 0.8475'

find_one = strings.find(' ')
find_two = strings[find_one:]

print(float(find_two))


# %% Kapitel 6 Aufgabe 6
# strip

txt = '        Dies ist ein kleiner Text mit zu viel leerzeichen am anfang und ende         '
x = txt.strip()
print(x)
y = b'www.example.com'.strip(b'cmowz.')
print(y)

# replace str.replace(old, new, count=-1)
txt2 = 'Das ist ein Test'
x = txt2.replace('Das', 'Was')
print(x)
y = x.replace('ist', 'dass den für')
print(y)