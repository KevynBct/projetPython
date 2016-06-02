#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv

#Connexion BDD
conn = sqlite3.connect('base.db')

# On vide la table 
cursor = conn.cursor()
cursor.execute("DROP table installation")
cursor.execute("DROP table activite")
cursor.execute("DROP table equipement")

#Creation des tables
    
#Table installation
cursor.execute("""
CREATE TABLE IF NOT EXISTS installation
(
    numero_instal INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nom VARCHAR, 
    numero INTEGER,
    adresse VARCHAR,
    ville VARCHAR
)
""")
conn.commit()


#Table equipement
cursor.execute("""
CREATE TABLE IF NOT EXISTS equipement(
     numero_equipement INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     nom VARCHAR,
     numero_installation INTEGER, 
     lat VARCHAR,
     long VARCHAR
)
""")
conn.commit()

#Table activite
cursor.execute("""
CREATE TABLE IF NOT EXISTS activite(
     id_activite INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, 
     numero_activite INTEGER,
     nom VARCHAR,
     numero_equipement INTEGER, 
     FOREIGN KEY(numero_equipement) REFERENCES equipement(numero_equipement)
 )
""")
conn.commit()



#Insertion data from equipement.csv
with open('csv/equipements.csv', 'r') as equip:
    reader = csv.reader(equip)

    #Flag pour eviter la lecture de la premiere ligne 
    first = True
    for row in reader:
        if first:
            first = False
            continue
        else:
            cursor.execute("INSERT INTO equipement(numero_equipement, nom, numero_installation, lat, long) VALUES (?, ?, ?, ?, ?)", (row[4],row[5],row[2], row[180],row[181]))
conn.commit()


#Insertion data from installations.csv
with open('csv/installations.csv', 'r') as instal:
    reader = csv.reader(instal)

    #Flag pour eviter la lecture de la premiere ligne 
    first = True
    for row in reader:
        if first:
            first = False
            continue
        else:
            cursor.execute("INSERT INTO installation(numero_instal, nom, adresse, ville) VALUES (?, ?, ?, ?)", (row[1],row[0],row[7],row[2]))
conn.commit()

#Insertion data from activite.csv
with open('csv/activites.csv', 'r') as act:
    reader = csv.reader(act)

    #Flag to avoid the first line
    first = True
    for row in reader:
        if first:
            first = False
            continue
        else:
            cursor.execute("INSERT INTO activite(numero_activite, nom, numero_equipement) VALUES (?, ?, ?)", (row[4], row[5], row[2]))
conn.commit()

#Close DataBase
conn.close()

