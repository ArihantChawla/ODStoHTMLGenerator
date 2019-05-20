from pyexcel_xls import get_data
from collections import OrderedDict
from row import rowhandling
#import json
data = OrderedDict()
data = OrderedDict(get_data("try.xlsx"))
#data = json.dumps(data)
#print(data)
data = data['Sheet1'] # len(data) = no. of rows in the xlsx file. Cols must be 12.
count=0
HTML = '<html>\n<body>\n<form>\n'
for i in data: # inside each row now
	HTML += '<div class="row">\n'
	HTML += rowhandling(i)
	HTML += '</div>\n'
HTML += '</form>\n'
HTML += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">'
HTML += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>'
HTML += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>'
HTML += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>'
HTML += '</body>\n</html>\n'
print(HTML)

