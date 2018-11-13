import openpyxl
from pprint import pprint

# Ah, the API has (largely) changed :p
#   (in comparison to the code shown in the book)
wkbook = openpyxl.load_workbook(filename='./src/sample_data.xlsx')

# shit down below
print(wkbook.sheetnames)    # also the new API

employee = wkbook['Employee']

# lazy-load trend, huh?
print(employee)         # Cell
print(employee.values)  # Cell's val

# Very, very basic usage ...
for i in employee.values:
	pprint(i)