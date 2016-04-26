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
	select * from equipement
	"""):
	print(row)

=======
for row in cursor.execute("""select * from equipement"""):
	
print(row)
>>>>>>> 4a6a57f4611cda5756002e93182e8b7d57fa737d
