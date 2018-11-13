import csv
from contextlib import ExitStack

with ExitStack() as stack:
	
	# Inspired by
	#   https://stackoverflow.com/a/26731825
	celebinfo_whole, celebinfo_partof = (
		stack.enter_context(open('./src/celeblist_write.csv', 'r')),
		stack.enter_context(open('./src/celeblist_write_partof.csv', 'w'))
	)
	
	reader = csv.DictReader(celebinfo_whole)
	writer = csv.writer(celebinfo_partof)

	for row in reader:
		
		if reader.line_num == 1:                # skip 'ID' col
			continue
			
		if row['DateOfBirth'][:4] != '1998':    # skip specific row
			writer.writerow([
				row['Name'],
				row['DateOfBirth'],
			])