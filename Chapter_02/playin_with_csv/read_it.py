import csv
from pprint import pprint

with open('./src/mylist.csv', mode='rt') as mycsv:
	reader = csv.DictReader(mycsv)
	
	for row in reader:
		print(row['first_name'], row['phone'], sep='\t')
		
	print('-' * 40)
	
	print(
		reader.fieldnames[:3],  # all col
		reader.line_num,        # current pos
		reader.dialect,         # fmt ('excel' here)
		sep='\n'
	)
	