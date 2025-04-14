# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 08:35:59 2025

@author: marcj
"""

# =============================================================================
#                           Reguläree Ausdrücke
# =============================================================================
# Wofür ? Suchen und Parsen von Zeichenketten 
# der Interpreter verwendet Regex um unsere Programme verstehen zu können

# Weitere Ressourcen 
# =============================================================================
# https://de.wikipedia.org/wiki/Regulärer_Ausdruck
# https://docs.python.org/library/re.html
# =============================================================================

# Bibliothek re 
# Einfachste Funktion zum finden eines Strings -> re.search()
# 
# Zeichen Wörterbuch:
# Zirkumflex        (ˆ)    -> Anfang einer Zeile 
# Punkt             (.)    -> Platzhalter  
# Stern             (*)    -> Null oder mehr Zeichen
# Plus              (+)    -> Eins oder mehr Zeichen
# Vorwardslash S    (\S)   -> Mindestens ein Zeichen, das kein Leerzeichen ist
#
#
#
#

# %% re.search() Beispiel 
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip() # alle Leerzeichenam Ende eines Strings entfernen
    if re.search('From:', line):        
        print(line)

# Zusatz infos zu .rstrip()
# Man kann mit rstrip aber auch spezifische angaben machen 
# z.B -> text = "Python123" -> print(text.rstrip("123")) -> A: "Python"

# %%
# Finde Zeilen, die mit 'From' beginnen
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line): 
        # Anfang einer Zeile finden (^) und nur From: Wenn am Anfang der Zeile steht
        print(line)
# %%
# =============================================================================
#  Wildcards -> Platzhalter
# =============================================================================

# Finde Zeilen die mit einem 'F' beginnen, gefolgt
# von 2 beliebigen Zeichen, gefolgt von einem 'm:'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)

# %%

# Finde Zeilen, die mit 'From' beginnen
# und ein at-Zeichen beinhalten
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)

# Diese Sonderzeichen bedeuten, dass sie nicht auf ein einzelnes Zeichen in 
# der Suchzeichenfolge passen, sondern auf null oder mehr Zeichen 
# (im Fall des Sterns) oder auf ein oder mehr der Zeichen (im Fall des Pluszeichens)

# %%
# =============================================================================
#  Extrahieren von Daten
# =============================================================================
# Daten aus einer Zeichenkette extrahieren -> .findall()

# Beispiel alle Emailadressen filtern
# =============================================================================
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Return-Path: <postmaster@collab.sakaiproject.org>
# for <source@collab.sakaiproject.org>;
# Received: (from apache@localhost)
# Author: stephen.marquard@uct.ac.za
# =============================================================================

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

# Der reguläre Ausdruck sucht nach Teilzeichenfolgen, die mindestens ein 
# NichtLeerzeichen enthalten, gefolgt von einem at-Zeichen, gefolgt von 
# mindestens einem weiteren Nicht-Leerzeichen. Das \S+ passt auf so viele 
# Nicht-Leerzeichen wie möglich.

# %%

# Finde Zeilen, die ein at-Zeichen zwischen zwei Zeichen haben: (Datei)
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)

# %%
# [a-zA-Z0-9]
# Dieser reguläre Ausdruck sucht nach Teilzeichenketten, die mit einem 
# einzigen Kleinbuchstaben, Großbuchstaben oder einer Zahl beginnen
# \S*@\S*
# gefolgt von keinem oder mehr Nicht-Leerzeichen (\S*)
# einem at-Zeichen, von keinem oder mehr Nicht-Leerzeichen (\S*) 
# [a-zA-Z]
# und schließlich von einem Groß- oder Kleinbuchstaben

# Finde Zeilen, mit einem at-Zeichen zwischen zwei Zeichen. Die
# Zeichenfolge vor dem at muss mit einem Buchstaben oder einer
# Ziffer beginnen; die Zeichenfolge nach dem at muss mit einem
# Buchstaben enden.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
        
# %%       
# =============================================================================
#  Kombination von Suchen und Extrahieren
# =============================================================================

# ^X-.*: [0-9.]+
# Wir wollen Zeilen, die mit X- beginnen, gefolgt
# von keinem oder mehr beliebigen Zeichen (.*), von einem Doppelpunkt (:) und dann
# einem Leerzeichen. Nach dem Leerzeichen suchen wir nach einem oder mehreren
# Zeichen, die entweder eine Ziffer (0-9) oder ein Punkt [0-9.]+ sind. Der Punkt
# innerhalb der eckigen Klammern stimmt mit einem tatsächlichen Punkt überein

# Finde Zeilen, die mit 'X' beginnen, gefolgt von beliebig vielen
# (nicht-Leer-)Zeichen, gefolgt von einem ':' und einem
# Leerzeichen. Danach kann eine Zahl mit einer oder mehreren
# Ziffern und Dezimalpunkten folgen.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)

# Die Zahlen extrahieren 
# Finde Zeilen, die mit 'X' beginnen, gefolgt von beliebig vielen
# (nicht-Leer-)Zeichen, gefolgt von einem ':' und einem
# Leerzeichen. Danach kann eine Zahl mit einer oder mehreren
# Ziffern und Dezimalpunkten folgen. Diese Zahl ist dann der Match.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        for num in x: 
            x = str(x[0])
            y = float(x)
            print(y, type(y))

# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%