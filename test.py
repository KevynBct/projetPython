#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

#Connexion BDD
conn = sqlite3.connect('base.db')

#Creation des tables
	
#Table installation
cursor = conn.cursor()

<<<<<<< HEAD
for row in cursor.execute("""
	select * from activite
	"""):
	print(row)

=======
for row in cursor.execute("""select * from equipement"""):
	print(row)
>>>>>>> d20d5eb8580e5c29007bbcfac94df2c29203dc91
