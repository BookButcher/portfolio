# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 15:43:39 2025

@author: marcj
"""

# %% Kapitel 7 Notizen + Übungen


# %% Datei suchen und öffnen
fhand = open('mbox.txt')
print(fhand)

# \n -> New Line Zeichen

# %% Jede Zeile zählen
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1   
print('Line Count:', count)

# %% Zeilen lesen
fhand = open('mbox-short.txt')
inputf = fhand.read()
print(len(inputf)) # Nur die zeichenlänge ausgeben

# %% Einen Teil ausgeben
print(inputf[:200])

# %% Nur bestimmte Teile ausgeben (email adressen)
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)

# %% Entfernt die Leerzeichen zwischen den Email adressen
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# %% Überspringt die unnötigen nicht gewollten Zeilen
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# %% Bestimmte Zeilen heraus suchen 
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue #verkürzte schreibweise
    print(line)
           
# %% Dateinamen durch Benutzer
fname = input('Gib eine Datei an: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print(f'Es gibt {count} Betreffzeilen in {fname}')


# %% Try und Except beim öffnen von Dateien 
fname = input('Gib eine Datei an: ')
try:
    fhand = open(fname)
    
except:
    print(f'Datei {fname} konnte nicht geoeffnet werden')
    exit()
    
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print(f'Es gibt {count} Betreffzeilen in {fname}')

  
# %% Schreiben von Dateien und auslesen 
fout = open('output.txt', 'w')
print(fout)
line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = 'the emblem of our land.\n'
fout.write(line2)

fout = open('output.txt')
inputf = fout.read()
print(inputf)

# %% schließen der Datei nach schreiben
fout.close()
 
# repr, hilft bei der Fehlersuche bei Leerzeichen Tabs etc 

# %% Kapitel 7 Aufgabe 1


outputtxt = open('mbox-short.txt')
readoutputtxt = outputtxt.read().upper()
print(readoutputtxt[:200])


# %% Kapitel 7 Aufgabe 2


count = 0
summary = 0
avg = 0

fname = input('Gib eine Datei an: ')
fhand = open(fname)


for line in fhand:
    line = line.rstrip()
    
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1                                  # zähler
        float_number = line.find(' ')               # finde die float number
        extract_number = line[float_number:]        # extrahiere sie aus allen zeilen
        convert_to_float = float(extract_number)    # konvertiere sie zu float
        summary += convert_to_float                 # Summiere alle Werte
        print(convert_to_float)    
      
        
avg = summary / count

          
print("Summe: ",round(summary, 2))       
print("Anzahl: ",count)
print("Durchschnitt: ", round(avg, 2)) 



# %% Kapitel 7 Aufgabe 3

count = 0
summary = 0
avg = 0
fname = input('Gib eine Datei an: ')

try:
    if fname == 'blablabla.txt':    
        print("Laberst du mich an ?")
        
    fhand = open(fname)
    
    for line in fhand:
        line = line.rstrip()
        
        if line.startswith('X-DSPAM-Confidence:'):
            count += 1                                  # zähler
            float_number = line.find(' ')               # finde die float number
            extract_number = line[float_number:]        # extrahiere sie aus allen zeilen
            convert_to_float = float(extract_number)    # konvertiere sie zu float
            summary += convert_to_float                 # Summiere alle Werte
            print(convert_to_float)    
          
    avg = summary / count
except: 
    print("Diese Datei existiert nicht !")
          
print("Summe: ",round(summary, 2))       
print("Anzahl: ",count)
print("Durchschnitt: ", round(avg, 2)) 

