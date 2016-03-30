import libs.csv as csv
with open('installations.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		print(', '.join(row))