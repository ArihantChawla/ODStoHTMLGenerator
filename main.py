from mergedcellsxlsx import ExtractMergedCellInfo
from pyexcel_xls import get_data
from collections import OrderedDict
from row import rowhandling
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
#import json
data = OrderedDict()
data = OrderedDict(get_data("try.xlsx"))
#data = json.dumps(data)
#print(data)
data = data['Sheet1'] # len(data) = no. of rows in the xlsx file. Cols must be 12.
mergedcells = ExtractMergedCellInfo("try.xlsx")
HTML = '<html>\n<body>\n<form>\n'
if len(mergedcells) != 0:
	for i in range(len(data)):
		HTML += '<div class="row">\n'
		for j in mergedcells:
			start_cell = j[0]
			start_cell = coordinate_from_string(start_cell)
			start_row = start_cell[1] -1
			start_col = column_index_from_string(start_cell[0]) -1
			if start_row ==  i:
				HTML += rowhandling(data[i],start_col,j[1])
				HTML += '</div>\n'
			else:
				HTML += rowhandling(data[i],-1,0)
				HTML += '</div>\n'

else:
	for i in data: # inside each row now
		HTML += '<div class="row">\n'
		HTML += rowhandling(i,-1,0)
		HTML += '</div>\n'

HTML += '</form>\n'
HTML += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
HTML += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>'
HTML += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>'
HTML += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>'
HTML += '</body>\n</html>\n'
print(HTML)

