#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv



#Connexion BDD
conn = sqlite3.connect('base.db')

#Creation des tables
    
#Table installation
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS installation(
     numero_instal INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     nom VARCHAR, 
     adresse VARCHAR, 
     code_postal VARCHAR,
     ville VARCHAR,
     latitude decimal,
     longitude decimal
)
""")
conn.commit()


#Table equipement
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS equipement(
     numero_equipement INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     nom VARCHAR,
     numero_installation INTEGER
)
""")
conn.commit()

#Table equipement_activite
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS equipement_activite(
     numero_equipement,
     numero_activite, 
     FOREIGN KEY(numero_equipement) REFERENCES equipement(numero_equipement),
     FOREIGN KEY(numero_activite) REFERENCES activite(numero_activite)
     
)
""")
conn.commit()

#Table activite
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS activite(
     numero_activite INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     nom VARCHAR
)
""")
conn.commit()

#Insertion des données dans la table à partir du fichier equipement.csv
with open('csv/equipements.csv', 'r') as equip:
    reader = csv.reader(equip)

    #Flag pour eviter la lecture de la premiere ligne 
    first = True
    for row in reader:
        if first:
            first = False
            continue
        else:
            cursor.execute("INSERT INTO equipement(numero_equipement, nom, numero_installation) VALUES(?, ?, ?)", (row[4],row[5],row[2]))

conn.commit()






#Fermeture BDD
conn.close()

