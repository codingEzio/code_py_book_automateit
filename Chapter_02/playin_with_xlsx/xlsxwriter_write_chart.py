import xlsxwriter

filename = __file__.replace('.py', '.xlsx')
wkbook = xlsxwriter.Workbook('./gen/' + filename)

wksheet = wkbook.add_worksheet()

data = [60, 40, 20, 20, 90, 130]

wksheet.write_column('A1', data)

chart = wkbook.add_chart({'type': 'line'})

chart.add_series({'values': '=Sheet1!$A$1:$A$6'})

wksheet.insert_chart('C1', chart)

wkbook.close()