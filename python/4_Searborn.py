# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:39:24 2025

@author: marcj

"""

# %%  Import

import seaborn as sns
import matplotlib.pyplot as plt
import warnings


# %% Daten 
tips = sns.load_dataset("tips") # Lödt das Dataset in die Variable tips
tips.head() # Gibt die ersten 5 Zeilen zurück


# %% Distribution Plots

import warnings
warnings.filterwarnings('ignore')

sns.displot(tips["total_bill"]) # Diagramm ausgabe über gesamte Rechnung

sns.displot(tips["total_bill"],kde=False,bins=30)
# bins = menge der plotsäulen
# kde = Historgramm aus/ein blenden

# %% jointplot

sns.jointplot(x="total_bill",y="tip",data=tips,kind="scatter")
# kind = Art des Diagramm

sns.jointplot(x="total_bill",y="tip",data=tips,kind="hex")

sns.jointplot(x="total_bill",y="tip",data=tips,kind="reg")

# %% pairplot

sns.pairplot(tips)

# palette = style 
# hue = wählt datensätze aus und vergleicht sie z.B männl. und weibl.
sns.pairplot(tips,hue='sex',palette='coolwarm')

# %% rugplot
# *rugplots* folgen eigentlich einem sehr simplen Konzept: 
# Sie zeichnen einfach einen Strich für jeden Piunkt einer 
# univariaten Verteilung. Sie sind ein Bestandteil eines KDE-Plots 

sns.rugplot(tips['total_bill'])

# %% PairGrid

iris = sns.load_dataset('iris')
iris.head()

# Das reine Grid
sns.PairGrid(iris)

# Dann können wir auf dem Grid zeichnen
g = sns.PairGrid(iris)
g.map(plt.scatter)

# Platzierungen mit upper, lower und diagonal
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

# %% pairplot

sns.pairplot(iris)
sns.pairplot(iris,hue='species',palette='rainbow')

# %% FacetGrid

tips = sns.load_dataset('tips')
tips.head()

g = sns.FacetGrid(tips, col="time", row="smoker")

g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, "total_bill")

g = sns.FacetGrid(tips, col="time",  row="smoker",hue='sex')

# Achtet darauf, dass die Argumente nach 
# plt.scatter geschrieben werden
g = g.map(plt.scatter, "total_bill", "tip").add_legend()

# %% JointGrid
# JointGrid ist die allgemeine Version für `jointplot()` Grid
g = sns.JointGrid(x="total_bill", y="tip", data=tips)

g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = g.plot(sns.regplot, sns.histplot)




# %% 
