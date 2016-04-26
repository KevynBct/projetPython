#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

#Connexion BDD
conn = sqlite3.connect('base.db')

#Creation des tables
	
#Table installation
cursor = conn.cursor()

for row in cursor.execute("""select * from equipement"""):
	print(row)
