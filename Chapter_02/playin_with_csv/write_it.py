import csv

# info collected from
#   https://www.imdb.com/list/ls064924680/
name = [
	'Kaitlyn Dever',
	'Dove Cameron',
	'Abigail Breslin',
	'Peyton List'
]

date_of_birth = [
	'1996-12-21',
	'1996-01-15',
	'1996-04-14',
	'1998-04-06'
]

if __name__ == '__main__':
	
	with open('./src/celeblist_write.csv', 'wt') as celeb_info:
		writer = csv.writer(celeb_info)
		
		writer.writerow(('ID', 'Name', 'DateOfBirth'))
		
		for i in range(len(name)):
			writer.writerow((
				i + 1,
				name[i],
				date_of_birth[i],
			))