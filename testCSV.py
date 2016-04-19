import libs.csv as csv

print("Choisissez un fichier :")
print ("1 - Installations")
print ("2 - Équipements")
print ("3 - Activités")
file = int(input())
print("Choisissez une colonne")
column = int(input())

if file == 1:
	with open('csv/installations.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in spamreader:
			# print(', '.join(row))
			print(row[column])
elif file == 2:
	with open('csv/equipements.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in spamreader:
			# print(', '.join(row))
			print(row[column])
elif file == 3:
	with open('csv/activités.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in spamreader:
			# print(', '.join(row))
			print(row[column])
else:
	print("Erreur")