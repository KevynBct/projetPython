#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This class tests data insertion. 

import sqlite3

#DB Connection
conn = sqlite3.connect('base.db')

	
#Print table activite
cursor = conn.cursor()
for row in cursor.execute("""
	select * from activite
	"""):
	print(row)

for row in cursor.execute("""select * from equipement"""):
	print(row)

