# -*- coding: utf-8 -*-

# %%
import random
for i in range(10):
    x = random.random()
    print(x)

for i in range(10):
    x = random.randint(1, 10)
    print(x)
      
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(t))


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
 
n1 = input("Gib Zahl 1 ein: ")
n2 = input("Gib Zahl 2 ein: ")

n1 = int(n1)
n2 = int(n2)

def addition(n1, n2):
    calc_add = n1 + n2
    return calc_add

x = addition(n1,n2)

def multiply(x):
    multi_calc = x * x 
    return multi_calc

y = multiply(x)
print(y)

# %% Kapitel 4 Aufgabe 1 - Übung 4

b = " Es zeigt den Beginn einer Funktion an"
print(b)

# %% Kapitel 4 Aufgabe 2 - Übung 5

d = "ABC", "Zap", "ABC"
print(d)

# %% Kapitel 4 Aufgabe 3 - Übung 6

eingabearbeitsstunden = input("Wie viele Stunden hast du gearbeitet: ") 
arbeitsstunden = float(eingabearbeitsstunden)
stundenlohn = 10

def lohnberechnung(arbeitsstunden, stundenlohn):
    if(arbeitsstunden > 40):
        basis = 40
        gesamtüberstunden = arbeitsstunden - basis
        lohnüberstunden = gesamtüberstunden * 1.4 * 10
        gesamt = lohnüberstunden + (basis * 10) 
        print("Monatsgehalt ", gesamt)
    else:
        gesamtnl = arbeitsstunden * 10
        print("Monatsgehalt ", gesamtnl)

lohnberechnung(arbeitsstunden, stundenlohn)


# %% Kapitel 4 Aufgabe 4 - Übung 7

eingabenote = input("Bitte gib eine Dezimalzahl zwischen 0,0 und 1,0 an: ")

def notenberechnung(eingabenote):
    
    try:   
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
            
    except:
        print("Fehler, nur Zahlen zwischen 0.0 und 1.0")
        
notenberechnung(eingabenote)


# %% Zusatz Map & Filter

def quadrat(num):
    return num ** 2

m_num = [1, 2, 3]

print(list(map(quadrat, m_num))) # Liste 


# oder 
for elem in map(quadrat, m_num):
    print(elem) # Einzelwerte

# Länge eines String auf gerade / ungerade testen 
def splicer(mein_string):
    if len(mein_string) % 2 == 0:
        return 'gerade'
    else:
        return 'ungerade', mein_string[0:]

namen = ['Rene', 'Marc', 'Peter', 'Jo']

print(list(map(splicer, namen)))

# Filter Funktion 
def ist_gerade(num):
    return num % 2 == 0

zahlen = [1, 2, 3, 4, 5, 6]

print(list(filter(ist_gerade, zahlen)))


# %% Lambda 
# Schrittweise vereinfachung 
# 1 
def quadrat(num):
    ergebnis = num ** 2
    
    return ergebnis

# 2
def quadrat(num): 
    return num ** 2

# 3
def quadrat(num): return num ** 2

print(quadrat(3))

# lambda 
lam_quad = lambda num: num ** 2
print(lam_quad(9))

# Weitere Beispiele 
range_zahlen = range(1,50)
list(filter(lambda num: num % 2 == 0, range_zahlen))


# Verschachtelte Anweisung und Reichweite




















