# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 08:59:23 2025

@author: marcj
"""

# =============================================================================
# Debugging Tipps aus Kapitel 1 - 15 
# =============================================================================
#%% Kapitel 1 
# Bei der Fehlersuche in einem Programm, insbesondere wenn wir
# an einem schwerwiegenden Fehler arbeiten, gibt es vier Dinge, die wir 
# versuchen sollten:

# Lesen Nochmal den Code durch erneutes Lesen prüfen. Haben wir alles so gesagt,
# wie wir es sagen wollten?

# Ausführen Man sollte einfach nochmal experimentieren, indem man nachverfolgbare 
# Änderungen vornimmt und verschiedene Versionen ausführt. Häufig wir
# das Problem offensichtlich, wenn wir es an der richtigen Stelle im Programm
# anzeigen lassen. Manchmal muss man etwas Zeit aufwenden, um ein gutes
# Gerüst zu bauen.

# Nachdenken Man sollte sich Zeit zum Nachdenken nehmen. Was für ein Fehler
# ist es? Handelt es sich um einen Syntaxfehler, einen Laufzeitfehler oder einen
# semantischen Fehler? Welche Informationen können wir aus den Fehlermeldungen 
# bzw. der Ausgabe des Programms entnehmen? Welche Art von Fehler
# könnte die Ursache sein für das Problem, das man sehen kann? Was haben
# wir zuletzt geändert, bevor das Problem auftrat?

# Rückzug Irgendwann ist es am besten sich zurückzuziehen und die letzten 
# Änderungen rückgängig zu machen, bis man wieder ein Programm hat, das
# funktioniert und das man verstehen kann. Dann kann man mit dem Neuaufbau 
# beginnen

# Um einen Fehler zu finden, muss man lesen, experimentieren,
# grübeln und sich manchmal zurückziehen

# Man muss sich Zeit zum Nachdenken nehmen
# Fehlersuche ist wie eine experimentell Wissenschaft. 
# Man sollte mindestens eine Hypothese darüber haben, was das Problem ist
    
# Eine Pause hilft beim Nachdenken. Das gilt auch für das Reden. Wenn man das
# Problem einer anderen Person (oder sogar sich selbst) erklärt, findet man 
# manchmal die Antwort, bevor man die Frage zu Ende gestellt hat

# Manchmal ist es am besten, sich zurückzuziehen und das Programm zu vereinfachen,
# bis man zu einem Ergebnis gelangt, welches funktioniert und man versteht

# Programmieranfänger zögern oft, sich zurückzuziehen, weil sie es nicht ertragen
# können eine Codezeile zu löschen (selbst wenn sie falsch ist). 

# Wenn man sich dadurch besser fühlt, sollte man einfach das Programm in eine 
# andere Datei sichern, bevor man es zerlegt. 

# Lösungsweg für die gesamte Aufgabe in kleinere Teilaufgaben einteilen. 
# Überlegen Sie sich bevor Sie mit dem Schreiben des Codes
# anfangen, welche logischen Teilfunktionen in Ihrer Aufgabe stecken. Und dann
# beginnen Sie, die erste Teilaufgabe zu lösen und – ganz wichtig – zu testen

# =============================================================================
#                           Thema Lernen 
# Das Buch ist zwar linear geschrieben und wenn man
# einen Kurs belegt, wird er auch linear verlaufen. Man sollte jedoch nicht zögern,
# sich dem Stoff sehr unlinear zu nähern. Egal ob vorwärts und rückwärts oder
# quer gelesen. Durch Überfliegen von fortgeschrittenem Material, ohne die Details
# vollständig zu verstehen, erhält man ein besseres Verständnis für das „Warum?“ der
# Programmierung. Durch Wiederholung früherer Inhalte und sogar Wiederholung
# früherer Übungen werden wir feststellen, dass wir tatsächlich viel gelernt haben,
# auch wenn das Material, welches wir gerade anstarren, ein wenig undurchdringlich
# erscheint
# =============================================================================

#%% Kapitel 2 Bezeichner, Ausdrücke und Anweisungen

# Zahlen dürfen nicht mit führenden Nullen beginnen 

# Häufige Fehler: Use before Definition -> Versuch eine Variable zu verwenden 
# bevor sie zugewiesen wurde

#%% Kapitel 3 Bedingte Ausführung

# Der Traceback, den Python beim Auftreten eines Fehlers anzeigt, enthält 
# eine Menge Informationen

# 1. welche Art von Fehler es war, und
# 2. wo er aufgetreten ist

#%% Kapitel 4 Funktionen

# Einrückung mit 4 Leerzeichen 
# Speichern vor ausführung

#%% Kapitel 5 Iterationen

# Möglichkeit zur Halbierung der Debugging Zeit ist das Bisektionieren
# Print Anweisungen in der nähe der mitte ausführen 

#%% Kapitel 6 Zeichenketten

# Fähigkeiten die man Programmieren kultivieren sollte ist sich zu fragen:
# Was könnte hier schiefgehen ?
# Welche verrückte Sache könnte der Benutzer tun, damit es abstürzt

# Beispiel: 
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
# Bei Leerzeichen eingabe gibt es einen Traceback Fehler aus 
# 2 möglichkeiten um das zu beheben ist: 
    #1. if line.startswith('#'): gibt False zurück wenn Zeichenkette leer
    #2. if len(line) > 0 and line[0] == '#': Einsatz von Wächter

#%% Kapitel 7 Dateien

# Beim Lesen und Schreiben von Dateien kann man auf Probleme mit Leerzeichen
# stoßen. Diese Fehler können schwer zu beheben sein, da Leerzeichen, Tabulatoren
# und Zeilenumbrüche normalerweise unsichtbar sind

# Die eingebaute Funktion repr kann helfen. Sie nimmt ein beliebiges Objekt als 
# Argument und gibt eine String-Repräsentation des Objekts zurück. Bei Zeichenketten
# stellt sie Leerzeichen mit Backslash-Sequenzen dar




#%% Kapitel 8 Listen

#%% Kapitel 9 Dictionarys

#%% Kapitel 10 Tupel

#%% Kapitel 11 Reguläre Ausdrücke

#%% Kapitel 12 Vernetzen von Programmen

#%% Kapitel 13 Web-Services

#%% Kapitel 14 Objektorientierte Programmierung

#%% Kapitel 15 Datenbanken und SQL

#%% Kapitel 16 Visualisierung von Daten

