from pyexcel_ods import get_data
from collections import OrderedDict
#import json
data = OrderedDict()
data = OrderedDict(get_data("try.ods"))
#data = json.dumps(data)
#print(data)
data = data['Sheet1'] # len(data) = no. of rows in the ods file. Cols must be 12.
count=0
for i in data: # inside each row now
	i = str(i)
	i = i[1:len(i)-1]
	i = i.split(", ")
	#print(i)
	for j in i:
		print(j) # inside cell now

