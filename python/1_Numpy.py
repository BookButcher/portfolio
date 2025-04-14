# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:53:59 2025

@author: marcj
"""

# %% Kapitel Numpy Imports
import numpy as np

# %% Kapitel Numpy Array anlegen

meine_liste = [1,2,3]
meine_liste
np.array(meine_liste)

# %% Kapitel Numpy 3 Dim Matrix
meine_matrix = [[1,2,3],[4,5,6],[7,8,9]]
meine_matrix
np.array(meine_matrix)

# %% Kapitel Numpy -> Methoden
# Gleichmäßig verteilte Werte, übergabe parameter von 0 bis 10 in 2er Schritten (11 = Exclusive)
np.arange(0,11,2)

# Zeros & Ones
np.zeros((5,5))

np.ones((3,3))

# Gibt gleichmäßig verteilte Zahlen eines bestimmten Intervalls zurück, von 0 bis 10, 50 Stk
np.linspace(0,10,50)

# Einheitsmatrix = 
np.eye(4)

# Random = Zufallszahlen
np.random.rand(5,5)

np.random.randint(1,100,10)

# Gibt ein Sample (oder mehrere) einer "standard normal" 
# Verteilung zurück. Anders als `rand`, dass gleichverteilt ist
np.random.randn(3,3)

# %% Kapitel Numpy Attribute und Methoden
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
print(arr)
print(ranarr)

# Gibt ein Array zurück, das dieselben Daten in neuer Form enthält
arr = np.arange(25)
print(arr.reshape(5,5))

# Max, argmax, min, argmin 
print(ranarr)
print(ranarr.max())
print(ranarr.argmax()) # -> Gibt nur den Index zurück von maximum
print(ranarr.min())
print(ranarr.argmin()) # -> Gibt nur den Index zurück von minimum

# Shape 
# Vektor
# Shape ist eines der Attribute, die Arrays haben. Es ist keine Methode.
# Gibt Dimension (Form) zurück
print(arr.shape)
print(arr.reshape(1,25))
print(arr.reshape(1,25).shape)
print(arr.reshape(25,1))

# Typ zurück geben
print(arr.dtype)

# %% Kapitel Numpy -> Indexing
print(arr)
print(arr[9])
# Werte in einem Bereich 
print(arr[0:5])

# Broadcasting = an bestimmten index bestimmte Werte festlegen 
arr[0:5]=100
print(arr)

# Array zurücksetzen 
arr = np.arange(25)
print(arr)

# teilstück auswählen
stueck_des_arr = arr[0:6]

# bearbeiten 
stueck_des_arr[:]=99
print(stueck_des_arr)
# Original Array
print(arr)


# Kopie erzeugen
arr_kopie = arr.copy()
print(arr_kopie)

# %% Kapitel Numpy Indexing in 2D Arrays
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)

# Die Reihe indexieren
print(arr_2d[1])

# Das Format ist arr_2d[row][col] oder arr_2d[row,col]
# Einzelne Elemente auswählen
arr_2d[1][0]
arr_2d[1,0]

# 2D Array Stücke auswählen
# Form (2,2) von oben rechts
arr_2d[:2,1:]

# %% Kapitel Numpy Raffiniertes Indexing
# erlaubt es ganze Reihen oder Spalten entgegen ihrer Reihenfolge zu wählen

# Eine Matrix erstellen
arr2d = np.zeros((10,10))
print(arr2d)

# Länge des Array
arr_laenge = arr2d.shape[1]
print(arr_laenge)

# Das Array erstellen
for i in range(arr_laenge):
    arr2d[i] = i
    
print(arr2d)
print('________________________________')

# raffiniertes Indexing  egal welche Richtung
print(arr2d[[2,4,6,8]])
print('________________________________')

print(arr2d[[6,4,8,2]])

# %% Kapitel Numpy Selection
# wie man Klammern nutzen kann, um eine Selection
# basieren auf Vergleichsoperatoren durchzuführen.

arr = np.arange(1,11)
print(arr)
boolarr = arr > 4
print(boolarr)
print(arr[boolarr])


# %% Kapitel Numpy Operations
print(arr)
print(arr + arr)
print(arr * arr)
print(arr - arr)
print(arr / arr) # -> Nur warnung kein Error
print(arr**3)


# Die Quadratwurzel ziehen
print(np.sqrt(arr))

# Den Exponent (e^) berechnen
print(np.exp(arr))

# Sinus
print(np.sin(arr))

# Logarithmus
print(np.log(arr))
