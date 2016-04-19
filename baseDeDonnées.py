#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3, csv

con = sqlite3.connect('base.db') # Connection et création de la base de données


# Import du fichier csv
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS equipements (col1, col2);")
with open('csv/equipements.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['col1'], i['col2']) for i in dr]
cur.executemany("INSERT INTO t (col1, col2, col3, col4, col5) VALUES (?, ?);", to_db)
con.commit()

con.close()