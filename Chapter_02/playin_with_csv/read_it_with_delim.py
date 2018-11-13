import csv
from write_it import name, date_of_birth

with open('./src/celeblist_write_withdelim.csv', 'w') as celebinfo:
	writer = csv.writer(
		celebinfo,
		delimiter='\t',         # 1 char only
		lineterminator='\n',    # as usual (not big difference)
	)
	
	writer.writerow(('ID', 'Name', 'DateOfBirth'))
	
	for i in range(len(name)):
		writer.writerow((
			i + 1,
			name[i],
			date_of_birth[i],
		))