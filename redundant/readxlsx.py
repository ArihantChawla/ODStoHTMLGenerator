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
for i in data: # inside each row now
	i = str(i)
	i = i[1:len(i)-1]
	i = i.split(", ")
#	print(i)
#	rowhandling(i)
#	for j in i:
	#	print(j) # inside cell now


