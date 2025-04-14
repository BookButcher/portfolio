# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:39:13 2025

@author: marcj
"""

# %% Matplotlib import
# Ist eine exzellente 2D und 3D Grafik Library um wissenschaftliche Diagramme zu erzeugen

import matplotlib.pyplot as plt
import numpy as np


# %% Daten anlegen
x = np.linspace(0, 5, 11)
y = x ** 2

x
y

# %% Einfaches Liniendiagamm

plt.plot(x, y, 'r') # 'r' bezeichnet die Farbe "Rot"
plt.xlabel('X Achsen Bezeichnung')
plt.ylabel('Y Achsen Bezeichnung')
plt.title('Diagramm Titel')
plt.show()

# %% plt.subplot(AnzahlDerZeilen, AnzahlDerSpalten, PlotNummer)

plt.subplot(1,2,1)
plt.plot(x, y, 'r--') 
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-'); 


# %% Einführung zur objektorientierten Methode

# Diagramm erstellen (leere Arbeitsfläche)
af = plt.figure()

# Dem Diagramm Achsen hinzufügen
axes = af.add_axes([0.1, 0.1, 0.8, 0.8]) # links, unten, breite, höhe (zwischen 0 und 1)

# Anhand dieser Achsen darstellen
axes.plot(x, y, 'b')
axes.set_xlabel('X Label definieren') # Nutzt set_ um die Methode zu beginnen
axes.set_ylabel('Y Label definieren')
axes.set_title('Titer definieren')


# Leere Arbeitsfläche erstellen
af = plt.figure()

axes1 = af.add_axes([0.1, 0.1, 0.8, 0.8]) # Hauptachse
axes2 = af.add_axes([0.2, 0.5, 0.4, 0.3]) # Eingesetzte Achse

# Größeres Diagramm mit Achse 1
axes1.plot(x, y, 'b')
axes1.set_xlabel('x Beschriftung Achse 1')
axes1.set_ylabel('y Beschriftung Achse 1')
axes1.set_title('Titel größeres Diagramm')

# Eingesetztes Diagramm mit Achse 2
axes2.plot(y, x, 'r')
axes2.set_xlabel('x Beschriftung Achse 2')
axes2.set_ylabel('y Beschriftung Achse 2')
axes2.set_title('Titel eingesetztes Diagramm');

# %% Subplots

# Wir nutzen wie bei plt.figure() 
diag, axes = plt.subplots()

# Jezt fügen wir über das axes Objekt weitere Informationen hinzu
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('titel');

# Leere Arbeitsfläche von 1 x 2 Subplots
diag, axes = plt.subplots(nrows = 1, ncols = 2)

# Axes ist ein Array der Achsen
axes

# durch dieses Array iterieren:
for ax in axes:
    ax.plot(x, y, 'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('titel')

# Anzeigen
diag

# %% diag.tight_layout() oder die plt.tight_layout() Methode nutzen
# Dadurch wird die Position der Achsen automatisch angepasst, 
# damit es keine überlappenden Inhalte mehr gibt

diag, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'g')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('titel')

diag    
plt.tight_layout()

# %% Diagrammgröße, Abbildungsverhältnis und DPI
diag = plt.figure(figsize=(8,4), dpi= 100)

ax = diag.add_axes([0,0,1,1])
ax.plot(x,y)

# Subplot
diag, axes = plt.subplots(figsize=(12,3))

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('titel');

# %% Diagramme speichern
diag.savefig("Desktop/dateiname.png")

# DPI einstellen
diag.savefig("Desktop/dateiname.png", dpi=200)

# %% Beschriftungen und Titel
# Diagramm Titel
ax.set_title("title")

# Achsenbeschriftung
ax.set_xlabel("x")
ax.set_ylabel("y")

# %% Legenden 

diag = plt.figure()

ax = diag.add_axes([0,0,1,1])

ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend()


# %% Legenden -> Einzelneinstellen

# Viele Optionen...

ax.legend(loc=1) # Ecke oben rechts
ax.legend(loc=2) # Ecke oben links
ax.legend(loc=3) # Ecke unten links 
ax.legend(loc=4) # Ecke unten rechts

# es gibt jedoch viele weitere Möglichkeiten

# Häufigste Verwendung
ax.legend(loc=0) # Matplotlib sucht sich die optimale Position selbst aus

# %% Farben festlegen, Linienstärke und Linientyp

# MatLab Style
diag, ax = plt.subplots()
ax.plot(x, x**2, 'b.-') # blaue Linie mit Punkten
ax.plot(x, x**3, 'g--') # grüne gestrichelte Linie

# Farben mit dem "color =" Parameter
diag, ax = plt.subplots()
ax.plot(x, x+1, color="blue", alpha=0.5) # Transparenz 50%
ax.plot(x, x+2, color="#8B008B")        # RGB Hex Code
ax.plot(x, x+3, color="#FF8C00")        # RGB Hex Code 
# %% Linien- und Markierungsstil

diag, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x+1, color="red", linewidth=0.25)
ax.plot(x, x+2, color="red", linewidth=0.50)
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)

# Mögliche Linienstile ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="green", lw=3, linestyle='-')
ax.plot(x, x+6, color="green", lw=3, ls='-.')
ax.plot(x, x+7, color="green", lw=3, ls=':')

# Benutzerdefinierte Querstrich
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10]) # Format: Linienlänge, Abstandslänge, ...

# Mögliche Markierungen: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
ax.plot(x, x+12, color="blue", lw=3, ls='--', marker='1')

# Markierungsgröße und Farbe
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green");


# %% Diagrammbereich

diag, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("Standard Achsen Bereich")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("Enge Achsen")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("Benutzerdefinierter Bereich");

# %% Spezielle Diagramme

plt.scatter(x,y)

from random import sample
data = sample(range(1, 1000), 100)
plt.hist(data)

# %% 

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Rechteckiges Box Plot
plt.boxplot(data,vert=True,patch_artist=True); 