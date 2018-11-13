import xlsxwriter

filename = __file__.replace('.py', '.xlsx')

wkbook = xlsxwriter.Workbook('./gen/' + filename)
wksheet = wkbook.add_worksheet(name='Expenses')

daily_expense = (
	['Brunch',  12],
	['Supper',  7],
	['Snack',   6],
)

row, col = 0, 0

for item, cost in (daily_expense):
	wksheet.write(row, col,     item)
	wksheet.write(row, col + 1, cost)
	row += 1

# It seems it does NOT workin' ('=SUM' in Preview),
#   it might be that I don't have a 'LibreOffice' (or not).

wksheet.write(row, 0, 'Total')
wksheet.write(row, 1, '=SUM(B1:B4)')

wkbook.close()