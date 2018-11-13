import csv

# caution:
#   do know what u're doin (specific use)
#   this might not get what u want (yep)
csv.register_dialect('my_own_dialect', delimiter='-')

with open('./src/celeblist_write.csv', 'r') as celebinfo:
	
	# ur own reader
	reader = csv.reader(celebinfo, dialect='my_own_dialect')
	
	for row in reader:
		print(row)